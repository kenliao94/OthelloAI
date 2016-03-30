# This is the main control loop of the game. Consider wrapping this game in an object. Much better design
from human import *
from ai import *
from board import *
from game import *
from config import *

#Init the game, initiating human, ai, board and logger
#p1 = AI(Piece.BLACK,AI_PROPERTY.RESPONSE_TIME,AI_PROPERTY.EASY_LEVEL)
p1 = Human(Piece.BLACK)
p2 = Human(Piece.WHITE)
board = Board([])
#start the game


game1 = Game("Game1",p1,p2,board)
game1.start()
game1.print_game_status()


