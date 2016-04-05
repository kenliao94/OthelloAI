from board import *
from config import *
from gametree import *
from heuristic import *
from logger import *


board_file = open("board.txt",'r')
index = 0
for line in board_file.readlines():
    #current player
    cur = Piece.BLACK
    board_list = convert_string_to_board(line)
    current_board = Board(board_list)
    print("Testing board")
    current_board.print_board()
    #Black player is the max in this testcase
    current_node = Node(current_board,cur)
    print("--------------------begin-------------------")
    print("Heuristic 1")
    print(heuristic_1(current_board,cur))
    print("Heuristic 2")
    print(heuristic_2(current_board,cur))
    print("Heuristic 3")
    print(heuristic_3(current_board,cur))
    print("Heuristic 4")
    print(heuristic_4(current_board,cur))
    print("Heuristic 5")
    print(heuristic_5(current_board,cur))
    print("--------------------end-------------------")
    index += 1