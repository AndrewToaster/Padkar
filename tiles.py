from typing import Callable
from basetypes import Tile, Unit, RenderData, Color, Position


class WallTile(Tile):
    def can_enter(self, unit: Unit):
        return False

    def on_draw(self, data: RenderData):
        data.text = "||"
        data.fg_color = Color(50, 255, 50)


class DelegateTile(Tile):
    def __init__(self, position: Position = None,
                 fcan_enter: Callable[[Tile, Unit], None] = None,
                 fon_enter: Callable[[Tile, Unit], None] = None,
                 fon_leave: Callable[[Tile, Unit], None] = None,
                 fon_draw: Callable[[Tile, RenderData], None] = None,
                 fon_tick: Callable[[Tile], None] = None):
        super().__init__(position)
        self._can_enter = fcan_enter
        self._on_enter = fon_enter
        self._on_leave = fon_leave
        self._on_draw = fon_draw
        self._on_tick = fon_tick

    def on_enter(self, unit: Unit):
        if self._on_enter:
            self._on_enter(self, unit)

    def on_leave(self, unit: Unit):
        if self._on_leave:
            self._on_leave(self, unit)

    def can_enter(self, unit: Unit):
        if self._can_enter:
            self._can_enter(self, unit)

    def on_draw(self, data: RenderData):
        if self._on_draw:
            self._on_draw(self, data)

    def on_tick(self):
        if self._on_tick:
            self._on_tick(self)
