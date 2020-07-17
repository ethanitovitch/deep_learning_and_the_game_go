import random

from dlgo.gotypes import Player, Point


def to_python(player_state):
    if player_state is None:
        return 'None'
    if player_state == Player.black:
        return Player.black
    return Player.white


MAX63 = 0x7fffffffffffffff

table = {}
empty_board = 0
for row in range(1, 20):
    for col in range(1, 20):
        for state in (Player.black, Player.white):
            code = random.randint(0, MAX63)
            table[Point(row, col), state] = code

from .gotypes import Player, Point

__all__ = ['HASH_CODE', 'EMPTY_BOARD']

HASH_CODE = {
    (pt, to_python(state)): hash_code for (pt, state), hash_code in table.items()
}

EMPTY_BOARD = empty_board

