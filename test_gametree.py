from board import *
from config import *
from gametree import *

def dummy_heur(board,player):
    #using the number of pieces heuristic
    piece_count = board.return_pieces_count()
    return piece_count[player]


current_board = Board()
#Black player is the max in this testcase
current_node = Node(current_board.board,Piece.BLACK)
value = minimax(current_node,0,3,dummy_heur,current_node.curPlayer,Piece.BLACK,Piece.WHITE)


