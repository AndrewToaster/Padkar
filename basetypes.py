from __future__ import annotations
from os import get_terminal_size
from typing import NamedTuple, ClassVar, Tuple, Dict
from termansi import fwrite, combine_modes, ColorRGB, GraphicMode, Terminal
from dataclasses import dataclass


class Color(NamedTuple):
    r: int
    g: int
    b: int


@dataclass(frozen=True)
class Position:
    UP: ClassVar[Position]
    DOWN: ClassVar[Position]
    LEFT: ClassVar[Position]
    RIGHT: ClassVar[Position]

    x: int
    y: int

    def __add__(self, other: Position):
        if not isinstance(other, Position):
            raise TypeError(f"Cannot apply + to {type(self)} and {type(other)}")

        return Position(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Position):
        if not isinstance(other, Position):
            raise TypeError(f"Cannot apply - to {type(self)} and {type(other)}")

        return Position(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Position | int):
        if isinstance(other, Position):
            return Position(self.x * other.x, self.y * other.y)
        elif isinstance(other, int):
            return Position(self.x * other, self.y * other)
        else:
            raise TypeError(f"Cannot apply * to {type(self)} and {type(other)}")

    def __floordiv__(self, other: Position | int):
        if isinstance(other, Position):
            return Position(self.x // other.x, self.y // other.y)
        elif isinstance(other, int):
            return Position(self.x // other, self.y // other)
        else:
            raise TypeError(f"Cannot apply // to {type(self)} and {type(other)}")

    def __truediv__(self, other: Position | int):
        return self.__floordiv__(other)

    def __neg__(self):
        return Position(-self.x, -self.y)


class Drawable:
    def on_draw(self, data: RenderData): ...


class Dirty:
    @property
    def is_dirty(self):
        return self._dirty

    @is_dirty.setter
    def is_dirty(self, value: bool):
        if self._dirty != value:
            self._dirty = value
            self.on_dirty_changed(value)

    def __init__(self, dirty: bool):
        self._dirty = dirty

    def on_dirty_changed(self, value: bool):
        ...


class RenderData:
    fg_color: Color | None = None
    bg_color: Color | None = None
    text: str | None = None

    @staticmethod
    def render(position: Position, data: RenderData):
        fwrite(Terminal.move_position(position.x * 2 + 1, position.y + 1),
               combine_modes(
                    ColorRGB.fg(*data.fg_color) if data.fg_color else GraphicMode.RESET_FG,
                    ColorRGB.bg(*data.bg_color) if data.bg_color else GraphicMode.RESET_BG),
               data.text or "  ")

    def __and__(self, other):
        if not isinstance(other, RenderData):
            raise TypeError("Expected RenderData, got " + str(type(other)))

        combined = RenderData()
        combined.fg_color = other.fg_color or self.fg_color
        combined.bg_color = other.bg_color or self.bg_color
        combined.text = other.text or self.text

        return combined


class Unit(Drawable):
    @property
    def position(self):
        return self.tile.position if self.tile else None

    def __init__(self):
        self.tile: Tile | None = None

    def on_enter(self, tile: Tile):
        ...

    def on_leave(self, tile: Tile):
        ...

    def on_contact(self, unit: Unit):
        ...

    def on_spawn(self, tile: Tile, _map: Map):
        ...

    def on_remove(self, _map: Map):
        ...

    def on_draw(self, data: RenderData):
        ...

    def on_tick(self):
        ...


class Tile(Drawable, Dirty):
    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value: Unit):
        if self._unit != value:
            self._unit = value
            self.is_dirty = True
            if value:
                self._unit.tile = self

    def __init__(self, position: Position = Position(0, 0)):
        super().__init__(True)
        self._unit: Unit | None = None
        self.position = position

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def can_enter(self, unit: Unit):
        return True

    def on_enter(self, unit: Unit):
        ...

    def on_leave(self, unit: Unit):
        ...

    def on_draw(self, data: RenderData):
        ...

    def on_tick(self):
        if self.unit:
            self.unit.on_tick()


class Camera:
    current: ClassVar[Camera] = None

    @property
    def origin(self):
        return self._origin

    @origin.setter
    def origin(self, value):
        self._origin = value
        self.render(True)

    @property
    def frustum(self):
        return self._frustum

    @frustum.setter
    def frustum(self, value):
        self._frustum = value

    def __init__(self, origin: Position = Position(0, 0), frustum: Tuple[int, int] = None):
        self._origin = origin
        self._frustum = frustum or Camera.get_frustum()

    def is_visible(self, position: Position):
        actual = self.origin + position
        frustum = Camera.get_frustum()
        return not (actual.x < 0 or actual.y < 0 or actual.x > frustum[0] or actual.y > frustum[1])

    def render(self, force=False):
        if force:
            fwrite(GraphicMode.RESET, Terminal.erase_screen())
        for tile in Map.current.tiles.values():
            if not Camera.current.is_visible(tile.position):
                continue

            if force or tile.is_dirty or (tile.unit and tile.unit.is_dirty):
                tile_data = RenderData()
                tile.on_draw(tile_data)
                if tile.unit:
                    unit_data = RenderData()
                    tile.unit.on_draw(unit_data)
                    tile_data = tile_data & unit_data
                    tile.unit.is_dirty = False
                RenderData.render(tile.position + self.origin, tile_data)
                tile.is_dirty = False
        fwrite(Terminal.MOVE_HOME)

    @staticmethod
    def get_frustum():
        x, y = get_terminal_size()
        return x // 2 * 2, y // 2 * 2


class Map:
    DEBUG: Map = None
    current: Map | None = None

    def __init__(self, tiles: Dict[Position, Tile]):
        for [pos, tile] in tiles.items():
            tile.position = pos

        self.tiles = tiles

    def tick(self):
        for tile in self.tiles.values():
            tile.on_tick()

    def tile_at(self, position: Position):
        return self.tiles[position] if position in self.tiles else None

    def try_move_unit(self, unit: Unit, position: Position):
        if unit.position == position:
            return True

        new_tile = self.tile_at(position)
        if not new_tile:
            return False
        if new_tile.unit:
            new_tile.unit.on_contact(unit)
            unit.on_contact(new_tile.unit)
            return False
        if not new_tile.can_enter(unit):
            return False

        old_tile = self.tile_at(unit.position)
        old_unit = old_tile.unit
        old_tile.unit = None
        new_tile.unit = old_unit
        old_tile.on_leave(unit)
        unit.on_leave(old_tile)
        new_tile.on_enter(unit)
        unit.on_enter(new_tile)

        return True

    def try_spawn_unit(self, unit: Unit, tile: Tile):
        if not tile or tile.unit or not tile.can_enter(unit):
            return False

        tile.unit = unit
        unit.on_spawn(tile, self)
        tile.on_enter(unit)
        unit.on_enter(tile)

    def try_remove_unit(self, unit: Unit):
        tile = self.tile_at(unit.position)
        if not tile:
            raise ValueError("Unit is not spawned")
        tile.on_leave(unit)
        unit.on_leave(tile)
        tile.unit = None
        unit.on_remove(self)


# Define constants
Position.UP = Position(0, -1)
Position.DOWN = Position(0, 1)
Position.LEFT = Position(-1, 0)
Position.RIGHT = Position(1, 0)
