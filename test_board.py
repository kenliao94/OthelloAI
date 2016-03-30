from board import *
new_board = Board()
new_board.print_board()
# print(new_board.get_possible_move(1))
# new_board.check_vertical((5, 3),1)
# new_board.check_horizontal((5, 3),1)
# new_board.check_diagonal((5, 3),1)

new_board.get_possible_move(1)
new_board.get_possible_move(2)


new_board.make_move((2, 4), 1)
new_board.print_board()
new_board.make_move((2, 3), 2)
new_board.print_board()

new_board.make_move((4, 2), 1)
new_board.print_board()
new_board.make_move((2, 5), 2)
new_board.print_board()


new_board.make_move((1, 5), 1)
new_board.print_board()
new_board.make_move((0, 5), 2)
new_board.print_board()

new_board.make_move((1, 6), 1)
new_board.print_board()
new_board.make_move((3, 5), 2)
new_board.print_board()

new_board.make_move((0, 6), 1)
new_board.print_board()
new_board.make_move((0, 7), 2)
new_board.print_board()

new_board.make_move((2, 6), 1)
new_board.print_board()
new_board.make_move((5, 2), 2)
new_board.print_board()