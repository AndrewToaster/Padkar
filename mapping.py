from __future__ import annotations
from typing import Dict
from basetypes import Tile, Position, Unit, RenderData, Camera
from tiles import WallTile


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
        if not new_tile or new_tile.unit or not new_tile.can_enter(unit):
            return False

        old_tile = self.tile_at(unit.position)
        new_tile.unit = old_tile.unit
        old_tile.unit = None
        new_tile.is_dirty = old_tile.is_dirty = True
        unit.position = position
        old_tile.on_leave(unit)
        unit.on_leave(old_tile)
        new_tile.on_enter(unit)
        unit.on_enter(new_tile)

        return True


__tile_map = {}
for x in range(10):
    for y in range(10):
        if x == 0 or y == 0 or x == 9 or y == 9:
            __tile_map[Position(x, y)] = WallTile()
        else:
            __tile_map[Position(x, y)] = Tile()

Map.DEBUG = Map(__tile_map)
del __tile_map
