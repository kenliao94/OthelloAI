from collector import *
from board import *
from config import *
from gametree import *

def dummy_heur(board,player):
    #using the number of pieces heuristic
    piece_count = board.return_pieces_count()
    return piece_count[player]

data = Collector('data.out')
current_board = Board()
#Black player is the max in this testcase
current_node = Node(current_board,Piece.BLACK)
# data.start_timer()
# value = minimax(current_node,0,2,dummy_heur,current_node.curPlayer,Piece.BLACK,Piece.WHITE)
# time_duration = data.end_timer()
# data.log_to_file("Time used by regular minimax:")
# data.log_to_file(str(time_duration))
#
# data.start_timer()
# value = minimax(current_node,0,3,dummy_heur,current_node.curPlayer,Piece.BLACK,Piece.WHITE)
# time_duration = data.end_timer()
# data.log_to_file("Time used by regular minimax:")
# data.log_to_file(str(time_duration))
#
# data.start_timer()
# value = minimax(current_node,0,4,dummy_heur,current_node.curPlayer,Piece.BLACK,Piece.WHITE)
# time_duration = data.end_timer()
# data.log_to_file("Time used by regular minimax:")
# data.log_to_file(str(time_duration))
#
# data.start_timer()
# value = minimax(current_node,0,5,dummy_heur,current_node.curPlayer,Piece.BLACK,Piece.WHITE)
# time_duration = data.end_timer()
# data.log_to_file("Time used by regular minimax:")
# data.log_to_file(str(time_duration))


# data.start_timer()
# value = minimax(current_node,0,8,dummy_heur,current_node.curPlayer,Piece.BLACK,Piece.WHITE)
# time_duration = data.end_timer()
# data.log_to_file("Time used by regular minimax:")
# data.log_to_file(str(time_duration))
# print(value)


#=====================================alphabeta=======================================================
# data.start_timer()
# value = alphabeta_minimax(current_node,0,2,dummy_heur,current_node.curPlayer,Piece.BLACK,Piece.WHITE,-1000000,1000000)# time_duration = data.end_timer()
# time_duration = data.end_timer()
# data.log_to_file("Time used by minimax with aplha beta pruning:")
# data.log_to_file(str(time_duration))
# print(value)
#
# data.start_timer()
# value = alphabeta_minimax(current_node,0,3,dummy_heur,current_node.curPlayer,Piece.BLACK,Piece.WHITE,-1000000,1000000)# time_duration = data.end_timer()
# time_duration = data.end_timer()
# data.log_to_file("Time used by minimax with aplha beta pruning:")
# data.log_to_file(str(time_duration))
# print(value)
#
# data.start_timer()
# value = alphabeta_minimax(current_node,0,4,dummy_heur,current_node.curPlayer,Piece.BLACK,Piece.WHITE,-1000000,1000000)# time_duration = data.end_timer()
# time_duration = data.end_timer()
# data.log_to_file("Time used by minimax with aplha beta pruning:")
# data.log_to_file(str(time_duration))
# print(value)
#
# data.start_timer()
# value = alphabeta_minimax(current_node,0,5,dummy_heur,current_node.curPlayer,Piece.BLACK,Piece.WHITE,-1000000,1000000)# time_duration = data.end_timer()
# time_duration = data.end_timer()
# data.log_to_file("Time used by minimax with aplha beta pruning:")
# data.log_to_file(str(time_duration))
# print(value)

# data.start_timer()
# value = alphabeta_minimax(current_node,0,6,dummy_heur,current_node.curPlayer,Piece.BLACK,Piece.WHITE,-1000000,1000000)# time_duration = data.end_timer()
# time_duration = data.end_timer()
# data.log_to_file("Time used by minimax with aplha beta pruning:")
# data.log_to_file(str(time_duration))
# print(value)
#
# data.start_timer()
# value = alphabeta_minimax(current_node,0,7,dummy_heur,current_node.curPlayer,Piece.BLACK,Piece.WHITE,-1000000,1000000)# time_duration = data.end_timer()
# time_duration = data.end_timer()
# data.log_to_file("Time used by minimax with aplha beta pruning:")
# data.log_to_file(str(time_duration))
# print(value)

data.start_timer()
value = alphabeta_minimax(current_node,0,8,dummy_heur,current_node.curPlayer,Piece.BLACK,Piece.WHITE,-1000000,1000000)# time_duration = data.end_timer()
time_duration = data.end_timer()
data.log_to_file("Time used by minimax with aplha beta pruning:")
data.log_to_file(str(time_duration))
print(value)
