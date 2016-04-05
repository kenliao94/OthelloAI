from board import *
from config import *
from gametree import *
from heuristic import *
from logger import *


board_file = open("board.txt",'r')
index = 0
for line in board_file.readlines():
    #current player
    print("--------------------begin-------------------")
    cur = (index % 2) + 1
    print("Current Player is {}. Black = 1 White = 2".format(cur))
    board_list = convert_string_to_board(line)
    current_board = Board(board_list)
    print("Testing board")
    current_board.print_board()
    #Black player is the max in this testcase
    print("Reg minimax")
    current_node = Node(current_board,cur)
    value = minimax(current_node,0,3,heuristic_1,current_node.curPlayer,Piece.BLACK,Piece.WHITE)
    print(value)
    print("Minimax with Alpha Beta")
    value = alphabeta_minimax(current_node,0,3,heuristic_1,current_node.curPlayer,Piece.BLACK,Piece.WHITE,-1000000,1000000)
    print(value)

    print("Testing its children")
    for possible_move in current_board.get_possible_move(cur):
        new_node = deepcopy(current_node)
        new_node.board.make_move(possible_move,cur)
        new_node.board.print_board()
        opponent = new_node.board.get_opposite_color(cur)
        new_node.curPlayer = opponent
        print("Max Player : {}".format(cur))
        print("Min Player : {}".format(opponent))
        value = alphabeta_minimax(new_node,0,2,heuristic_5,opponent,cur,opponent,-1000000,1000000)
        print(value)
    print("--------------------end-------------------")
    index += 1