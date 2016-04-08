from board import *
from config import *
from copy import *


def heuristic_1(board,color):
    """
    :param board: A board object
    :param color: Used to indicate which player
    :return: a heuristic value which shows the difference between the number of disks in this color and
             the number of disks in the other color
    """
    color_player = 0
    oppo_player = 0

    opponent = board.get_opposite_color(color)
    for row in range(8):
        for column in range(8):
            if board.board[row][column] == color:
                color_player += 1
            elif board.board[row][column] == opponent:
                oppo_player += 1
    return color_player - oppo_player




def heuristic_2_one_side(board,color):
    score = 0
    #count the number of pieces on the edge, give it a score, on the corner give it a score, centre give it a score
    #corner
    cur_board = board.board
    if board.board[0][0] == color:
        score += Constant.corner

    if board.board[0][7] == color:
        score += Constant.corner

    if board.board[7][0] == color:
        score += Constant.corner

    if board.board[7][7] == color:
        score += Constant.corner

    #count the number of pieces on the edge
    for i in range(1,7):
        if cur_board[0][i] == color:
            score += Constant.edge
    for i in range(1,7):
        if cur_board[7][i] == color:
            score += Constant.edge
    for i in range(1,7):
        if cur_board[i][0] == color:
            score += Constant.edge
    for i in range(1,7):
        if cur_board[i][7] == color:
            score += Constant.edge

    #count centre pieces
    for i in range(1,7):
        for q in range(1,7):
            if cur_board[i][q] == color:
                score += Constant.centre

    return score

def heuristic_2(board,player):
    opponent = board.get_opposite_color(player)
    return heuristic_2_one_side(board,player) - heuristic_2_one_side(board,opponent)


def heuristic_3(board,color):
    """
    :param board: A board object
    :param color: Used to indicate which player
    :return: Assume playerA has this color disks, a heuristic value is returned to show how stable this state is for playerA
             who has this color disks. Pieces which belong to playerA and might be flanked by the opponent right after player's turn will be set
             to unstable. Pieces will NOT be flanked by the opponent right after player's turn will be set
             to stable_unknown. Pieces at the corner in the grid will be set to stable.
    """
    opponent = board.get_opposite_color(color)
    return heuristic_3_one_side(board,color) - heuristic_3_one_side(board,opponent)

def heuristic_3_one_side(board,color):
    """
    :param board: A board object
    :param color: Used to indicate which player
    :return: Assume playerA has this color disks, a heuristic value is returned to show how stable this state is for playerA
             who has this color disks. Pieces which belong to playerA and might be flanked by the opponent right after player's turn will be set
             to unstable. Pieces will NOT be flanked by the opponent right after player's turn will be set
             to stable_unknown. Pieces at the corner in the grid will be set to stable.
    """
    opponent = board.get_opposite_color(color)
    number_of_disks_for_player_has_color = 0
    non_repeated_affected_pieces = []
    corner = 0
    for row in range(8):
        for column in range(8):
            if board.board[row][column] == color:
                number_of_disks_for_player_has_color += 1
                if (row == 0 and column == 0) or (row == 0 and column == 7) or (row == 7 and column == 0) or (row == 7 and column == 7):
                    corner += 1
            elif board.board[row][column] == opponent:
                continue
            else:
                affected_pieces_for_player_has_color = board.get_affected_pieces((row, column),opponent)

                for piece in affected_pieces_for_player_has_color:
                    if piece not in non_repeated_affected_pieces:
                        non_repeated_affected_pieces.append(piece)

    statable_unknown = number_of_disks_for_player_has_color - len(non_repeated_affected_pieces)

    return corner * Constant.stable + len(non_repeated_affected_pieces) * Constant.unstable + statable_unknown * Constant.stable_unknown

def collect_points(board,color):
    """
    :param board: A board object
    :param color: Used to indicate which player
    :return: set each square in the grid a level, set each level a number, the closer the piece to the
             nearest boundary, the higher the level is, return the sum of numbers representing levels for
             player who has this color disks

              # column_0  column_1 column_2 column_3 column_4 column_5 column_6 column_7

    #row_0   # [level_5, level_0, level_4, level_4, level_4, level_4, level_0, level_5]

    #row_1   # [level_0, level_0, level_3, level_3, level_3, level_3, level_0, level_0]

    #row_2   # [level_4, level_3, level_2, level_2, level_2, level_2, level_3, level_4]

    #row_3   # [level_4, level_3, level_2, level_1, level_1, level_2, level_3, level_4]

    #row_4   # [level_4, level_3, level_2, level_1, level_1, level_2, level_3, level_4]

    #row_5   # [level_4, level_3, level_2, level_2, level_2, level_2, level_3, level_4]

    #row_6   # [level_0, level_0, level_3, level_3, level_3, level_3, level_0, level_0]

    #row_7   # [level_5, level_0, level_4, level_4, level_4, level_4, level_0, level_5]

    """
    total = 0
    for row in range(8):
        for column in range(8):
            if board.board[row][column] == color:

                if (row == 0 and column == 1) or (row == 0 and column == 6) or (row == 1 and column == 0) or \
                        (row == 1 and column == 1) or (row == 1 and column == 6) or (row == 1 and column == 7) \
                        or (row == 6 and column == 0) or (row == 6 and column == 1) or (row == 6 and column == 6) or \
                        (row == 6 and column == 7) or (row == 7 and  column == 1) or (row == 7 and column == 6):
                    total += Constant.level_0
                elif (row == 0 and column == 0) or (row == 7 and column == 0) or (row == 0 and column == 7) or (row == 7 and column == 7):

                    total += Constant.level_5
                elif (row == 0 and column in range(1, 7)) or (row == 7 and column in range(1, 7)) or (column == 0 and row in range(1, 7)) or (column == 7 and row in range(1, 7)):

                    total += Constant.level_4
                elif (row == 1 and column in range(1, 7)) or (row == 6 and column in range(1, 7)) or (column == 1 and row in range(1, 7)) or (column == 6 and row in range(1, 7)):

                    total += Constant.level_3
                elif (row == 2 and column in range(2, 6)) or (row == 5 and column in range(2, 6)) or (column == 2 and row in range(2, 6)) or (column == 5 and row in range(2, 6)):

                    total += Constant.level_2
                else:

                    total += Constant.level_1

    return total

def heuristic_4(board,color):
    """
    :param board: A board object
    :param color: Used to indicate which player
    :return: a heuristic value which shows the difference between the number of possible moves for player who has this color disks and
             the number of possible moves for the opponent at this state
    """
    opponent = board.get_opposite_color(color)
    return heuristic_4_one_side(board,color) - heuristic_4_one_side(board,opponent)

def heuristic_4_one_side(board,color):
    """
    :param board: A board object
    :param color: Used to indicate which player
    :return: a heuristic value which shows the difference between the number of possible moves for player who has this color disks and
             the number of possible moves for the opponent at this state
    """
    total = 0

    for possible_move in board.get_possible_move(color):
        new_board = deepcopy(board)

        new_board.make_move(possible_move,color)

        point_collected = collect_points(new_board,color)

        total += point_collected

    return total


def heuristic_5(board,color):
    """
    :param board: A board object
    :param color: Used to indicate which player
    :return: a heuristic value which shows the difference between the number of possible moves for player who has this color disks and
             the number of possible moves for the opponent at this state
    """
    opponent = board.get_opposite_color(color)
    return heuristic_5_one_side(board,color) - heuristic_5_one_side(board,opponent)

def heuristic_5_one_side(board,color):
    """
    :param board: A board object
    :param color: Used to indicate which player
    :return: a heuristic value which shows the difference between the number of unoccupied squares adjacent to a disk in opponent's color
             and the number of unoccupied squares adjacent to a disk in color

    """
    opponent = board.get_opposite_color(color)
    unoccupied_squares_adjacent_to_opponent_player = 0


    for row in range(1,7):
        for col in range(1,7):
            if board.board[row][col] == Piece.VOID:
                if board.board[row-1][col-1] == opponent or board.board[row-1][col] == opponent or board.board[row-1][col+1] == opponent or \
                     board.board[row][col-1] == opponent or board.board[row][col+1] == opponent or \
                    board.board[row+1][col-1] == opponent or board.board[row+1][col] == opponent or board.board[row+1][col+1] == opponent:

                    unoccupied_squares_adjacent_to_opponent_player += 1


    for col in range(1, 7):
        row = 0
        if board.board[row][col] == Piece.VOID:
            if board.board[row][col-1] == opponent or board.board[row][col+1] == opponent or \
                    board.board[row+1][col-1] == opponent or board.board[row+1][col] == opponent or board.board[row+1][col+1] == opponent:

                    unoccupied_squares_adjacent_to_opponent_player += 1


    for col in range(1, 7):
        row = 7
        if board.board[row][col] == Piece.VOID:
            if board.board[row][col-1] == opponent or board.board[row][col+1] == opponent or \
                    board.board[row-1][col-1] == opponent or board.board[row-1][col] == opponent or board.board[row-1][col+1] == opponent:

                    unoccupied_squares_adjacent_to_opponent_player += 1


    for row in range(1, 7):
        col = 0
        if board.board[row][col] == Piece.VOID:
            if board.board[row-1][col] == opponent or board.board[row-1][col+1] == opponent or \
                    board.board[row][col+1] == opponent or board.board[row+1][col] == opponent or board.board[row+1][col+1] == opponent:

                    unoccupied_squares_adjacent_to_opponent_player += 1


    for row in range(1, 7):
        col = 7
        if board.board[row][col] == Piece.VOID:
            if board.board[row-1][col-1] == opponent or board.board[row-1][col] == opponent or \
                    board.board[row][col-1] == opponent or board.board[row+1][col-1] == opponent or board.board[row+1][col] == opponent:

                    unoccupied_squares_adjacent_to_opponent_player += 1


    if board.board[0][0] == Piece.VOID:
        if board.board[0][1] == opponent or board.board[1][0] == opponent or board.board[1][1] == opponent:

            unoccupied_squares_adjacent_to_opponent_player += 1


    if board.board[0][7] == Piece.VOID:
        if board.board[0][6] == opponent or board.board[1][6] == opponent or board.board[1][7] == opponent:

            unoccupied_squares_adjacent_to_opponent_player += 1


    if board.board[7][0] == Piece.VOID:
        if board.board[6][0] == opponent or board.board[6][1] == opponent or board.board[7][1] == opponent:

            unoccupied_squares_adjacent_to_opponent_player += 1


    if board.board[7][7] == Piece.VOID:
        if board.board[6][6] == opponent or board.board[6][7] == opponent or board.board[7][6] == opponent:

            unoccupied_squares_adjacent_to_opponent_player += 1


    return unoccupied_squares_adjacent_to_opponent_player


