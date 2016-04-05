# This is the main control loop of the game. Consider wrapping this game in an object. Much better design
from human import *
from ai import *
from board import *
from game import *
from config import *
from collector import *

#Init the game, initiating human, ai, board and logger
#p1 = Human(Piece.BLACK)
p1 = AI(Piece.BLACK,heuristic_1,2)
p2 = AI(Piece.WHITE,heuristic_5,7)
board = Board([])
data_collector = Collector("data.out")
#start the game
game1 = Game("Game1",p1,p2,board,data_collector)
game1.start()
game1.print_game_status()


