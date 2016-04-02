# This file define a set of enum and constant used
# Enum for piece color
class Piece:
    BLACK = 1
    WHITE = 2
    VOID = 3
    TIE = 4

class Player:
    FIRST = 1
    SECOND = 2

class Board_Property:
    BOARD_SIZE = 8

class AI_PROPERTY:
    EASY_LEVEL = 1
    MEDIUM_LEVEL = 2
    HARD_LEVEL = 3
    RESPONSE_TIME = 1

class Constant:
    search_level = 3
    tie_value = 15
    max_player_endgame_value = 1000
    min_player_endgame_value = -1000





