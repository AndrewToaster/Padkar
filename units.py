from typing import Callable
from basetypes import Unit, Map, Position, Tile, RenderData


class DelegateUnit(Unit):
    def __init__(self,
                 fon_spawn: Callable[[Unit, Tile, Map], None] = None,
                 fon_remove: Callable[[Unit, Map], None] = None,
                 fon_contact: Callable[[Unit, Unit], None] = None,
                 fon_enter: Callable[[Unit, Tile], None] = None,
                 fon_leave: Callable[[Unit, Tile], None] = None,
                 fon_draw: Callable[[Unit, RenderData], None] = None,
                 fon_tick: Callable[[Unit], None] = None):
        super().__init__()
        self._on_spawn = fon_spawn
        self._on_remove = fon_remove
        self._on_contact = fon_contact
        self._on_enter = fon_enter
        self._on_leave = fon_leave
        self._on_draw = fon_draw
        self._on_tick = fon_tick

    def on_enter(self, tile: Tile):
        if self._on_enter:
            self._on_enter(self, tile)

    def on_leave(self, tile: Tile):
        if self._on_leave:
            self._on_leave(self, tile)

    def on_contact(self, unit: Unit):
        if self._on_contact:
            self._on_contact(self, unit)

    def on_spawn(self, tile: Tile, _map: Map):
        if self._on_spawn:
            self._on_spawn(self, tile, _map)

    def on_remove(self, _map: Map):
        if self._on_remove:
            self._on_remove(self, _map)

    def on_draw(self, data: RenderData):
        if self._on_draw:
            self._on_draw(self, data)

    def on_tick(self):
        if self._on_tick:
            self._on_tick(self)


class Collectible(Unit):
    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def can_pickup(self, unit: Unit):
        return True

    # noinspection PyMethodMayBeStatic
    def on_pickup(self, unit: Unit):
        Map.current.try_remove_unit(self)

    def on_contact(self, unit: Unit):
        if self.can_pickup(unit):
            self.on_pickup(unit)
