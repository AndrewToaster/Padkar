from __future__ import annotations
from basetypes import Tile, Position, Map
from tiles import WallTile

DEBUG_MAP = {}
for x in range(10):
    for y in range(10):
        if x == 0 or y == 0 or x == 9 or y == 9:
            DEBUG_MAP[Position(x, y)] = WallTile()
        else:
            DEBUG_MAP[Position(x, y)] = Tile()

DEBUG_MAP = Map(DEBUG_MAP)
