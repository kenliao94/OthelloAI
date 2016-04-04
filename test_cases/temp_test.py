from logger import *
from board import *

new_board = Board()
s = convert_board_to_string(new_board.board)
log_to_file(s,'out.txt')

b = convert_string_to_board(s)
print(b)