from board import *
from config import *
from gametree import *
from heuristic import *
from logger import *

board = convert_string_to_board("3333333333333333333333333331233333312333333123333333113333333133")
current_board = Board(board)
current_board.print_board()
current_node = Node(current_board,Piece.WHITE)
value = alphabeta_minimax(current_node,0,3,heuristic_1,Piece.WHITE,Piece.WHITE,Piece.BLACK,-1000000,1000000)
print(value)
print(current_node.board.get_possible_move(Piece.WHITE))
#White turn
