# This is the main control loop of the game. Consider wrapping this game in an object. Much better design
from human import *
from ai import *
from board import *
from logger import *
from config import *

#Init the game, initiating human, ai, board and logger


#Actually play the game
game_end = False
current_round = Player.FIRST
while game_end:
    board.print_broad() #Displaying the board
    #First player move, can be either AI or human
    if current_round == Player.FIRST:
        move_is_valid = False
        while not move_is_valid:
            move = p1.thinking(board.get_board())
            move_is_valid = board.make_move(move,p1.color)
        current_round = Player.SECOND
    else:
        move_is_valid = False
        while not move_is_valid:
            move = p2.thinking(board.get_board())
            move_is_valid = board.make_move(move,p2.color)
        current_round = Player.FIRST

    if board.check_end_game():
        game_end = True #game end

#POST Game
#Annouce winner
winner = board.get_winner()
stars = logger.get_stats()

