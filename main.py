from __future__ import annotations
from platform import system
from sys import exit, stdout
from basetypes import *
import mapping
from collectibles import KeyPickup
from termansi import *
from units import DelegateUnit

if not stdout.isatty():
    print("STDOUT is not a terminal")
    exit(1)

# Old windows console is dog poo-poo, enable VT_SEQUENCES
if system() == "Windows":
    Utils.vt_seq_win(True)

fwrite(Terminal.erase_screen())


def __on_draw(self: Unit, data: RenderData):
    data.text = "PP"
    data.bg_color = Color(255, 0, 0)


Map.current = mapping.DEBUG_MAP
player = DelegateUnit(fon_draw=__on_draw)
key = KeyPickup()
Map.current.try_spawn_unit(player, Map.current.tile_at(Position(1, 1)))
Map.current.try_spawn_unit(key, Map.current.tile_at(Position(5, 1)))

Camera.current = Camera()

while True:
    Camera.current.render()
    Map.current.tick()

    inp = Utils.getch()
    if inp == b'\x03':  # If we receive ETX (End of Text) we exit with code 0
        exit(0)
    elif inp == b'w':
        Map.current.try_move_unit(player, player.position + Position.UP)
    elif inp == b's':
        Map.current.try_move_unit(player, player.position + Position.DOWN)
    elif inp == b'a':
        Map.current.try_move_unit(player, player.position + Position.LEFT)
    elif inp == b'd':
        Map.current.try_move_unit(player, player.position + Position.RIGHT)
    elif inp == b't':
        Camera.current.origin += Position.UP
    elif inp == b'g':
        Camera.current.origin += Position.DOWN
    elif inp == b'f':
        Camera.current.origin += Position.LEFT
    elif inp == b'h':
        Camera.current.origin += Position.RIGHT



