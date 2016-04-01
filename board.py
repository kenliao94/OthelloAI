#we define the board object here
from config import *

class Board:

    def __init__(self,board = []):
        '''
        This function should create the board, in this case, it is represented as a 2D array with
        starter position. The board size is defined in config.py

        Note : The board index from 0 to 7 Board[][] is indexed as row x column
        '''
        if board == []:
            board = [[Piece.VOID, Piece.VOID, Piece.VOID, Piece.VOID, Piece.VOID, Piece.VOID, Piece.VOID, Piece.VOID],
                     [Piece.VOID, Piece.VOID, Piece.VOID, Piece.VOID, Piece.VOID, Piece.VOID, Piece.VOID, Piece.VOID],
                     [Piece.VOID, Piece.VOID, Piece.VOID, Piece.VOID, Piece.VOID, Piece.VOID, Piece.VOID, Piece.VOID],
                     [Piece.VOID, Piece.VOID, Piece.VOID, Piece.BLACK, Piece.WHITE, Piece.VOID, Piece.VOID, Piece.VOID],
                     [Piece.VOID, Piece.VOID, Piece.VOID, Piece.WHITE, Piece.BLACK, Piece.VOID, Piece.VOID, Piece.VOID],
                     [Piece.VOID, Piece.VOID, Piece.VOID, Piece.VOID, Piece.VOID, Piece.VOID, Piece.VOID, Piece.VOID],
                     [Piece.VOID, Piece.VOID, Piece.VOID, Piece.VOID, Piece.VOID, Piece.VOID, Piece.VOID, Piece.VOID],
                     [Piece.VOID, Piece.VOID, Piece.VOID, Piece.VOID, Piece.VOID, Piece.VOID, Piece.VOID, Piece.VOID]]
        self.board = board

        return


    def make_move(self,coordinate_tuple,color):
        '''
        It will make a move and change the board accordingly. The color is the current player
        Example:
            Input : Board.make_move((1,2),Piece.Black) or Board.make_move((1,2),Player.color)
            The first parameter is a coordinate in the type of tuple, second parameter is an enum to color

            This code should change the board based on that move, i.e if I call Board.make_move(3,5),
            then the white piece at (3,4) will change

            Output : 1 if succeeded, 0 if failed
        '''
        #print('here is the coordinate cuple in make move : ' + str(coordinate_tuple) + ' by player' + str(color))
        all = []
        vertical = self.check_vertical(coordinate_tuple,color)
        # print('vertical '+str(vertical))
        horizontal = self.check_horizontal(coordinate_tuple,color)
        # print('horizontal '+str(horizontal))
        diagonal = self.check_diagonal(coordinate_tuple,color)
        # print('diagonal '+str(diagonal))
        all.extend(vertical)
        all.extend(horizontal)
        all.extend(diagonal)
        # print('all '+str(all))
        if len(all) == 0:
            return 0

        self.board[coordinate_tuple[0]][coordinate_tuple[1]] = color
        for piece in all:

            self.board[piece[0]][piece[1]] = color


        return 1

    def get_possible_move(self,color):
        '''
        Return a list of coordinate_tuple that the current player (with color) can play. If not possible then empty
        Example :
            Input:
                Board.get_possible_move(Piece.Black)
            Output:
                [(3,5),(2,4),(4,2),(5,3)]  //Refer to the board in the init method

            Note : Please don't change the board, i.e don't make change to the board array, just read
        '''
        #Right now, screw run time, just get it to work. Do Linear search

        possible_move = []
        for row in range(8):
            for column in range(8):
                if self.board[row][column] == Piece.BLACK or self.board[row][column] == Piece.WHITE:
                    #space already occupied
                    continue
                else:
                    #space is void
                    if len(self.check_vertical((row,column),color)) != 0:
                        possible_move.append((row,column))
                        continue
                    if len(self.check_horizontal((row,column),color)) != 0:
                        possible_move.append((row,column))
                        continue
                    if len(self.check_diagonal((row,column),color)) != 0:
                        possible_move.append((row,column))
        #print('possible moves: ' + str(possible_move))
        return possible_move

    #End Game
    def check_end_game(self):
        """
        This function is called to see if the board is filled
        Example :
            Input : None
            Output : true if it is ended, false if not

            Cases :
            1. The board is filled
            2. There is only one color (i.e, even the board is not filled, there is a possiblity that
            black gets wiped out, hence white wins)

        """
        # pieces_count : {Piece.BLACK: num, Piece.WHITE : num, Piece.VOID : num}
        pieces_count = self.return_pieces_count()

        if pieces_count[Piece.VOID] == 0 or pieces_count[Piece.BLACK] == 0 or pieces_count[Piece.WHITE] == 0:
            return True
        return False

    #Internal routine for make_move
    def check_vertical(self,coordinate_tuple,color):
        """
        return all pieces need to be flipped at this column (up and down)
        """
        result = []
        affected_pieces = []
        row_count = coordinate_tuple[0]
        opposite_color = self.get_opposite_color(color)
        #check the pieces on top of coordinate_tuple in the same column, hence the number column_count goes down
        while row_count > 0:
            # check the one on the left side of it, hence decrementing
            row_count -= 1
            if self.board[row_count][coordinate_tuple[1]] == color:
                if len(affected_pieces) > 0:
                    result.extend(affected_pieces)
                break
            elif self.board[row_count][coordinate_tuple[1]] == opposite_color:
                affected_pieces.append((row_count, coordinate_tuple[1]))
                continue
            elif self.board[row_count][coordinate_tuple[1]] == Piece.VOID:
                #again generating an invalid move
                break
            else:
                raise NameError("Unexpected case at check_vertical, up case")

        #check the pieces underneath coordinate_tuple in the same column, hence the number column_count goes up
        row_count = coordinate_tuple[0]
        affected_pieces = []
        while row_count < 7:
            # check the one on the left side of it, hence decrementing
            row_count += 1
            if self.board[row_count][coordinate_tuple[1]] == color:
                if len(affected_pieces) > 0:
                    result.extend(affected_pieces)
                break
            elif self.board[row_count][coordinate_tuple[1]] == opposite_color:
                affected_pieces.append((row_count, coordinate_tuple[1]))
                continue
            elif self.board[row_count][coordinate_tuple[1]] == Piece.VOID:
                #again generating an invalid move
                break
            else:
                raise NameError("Unexpected case at check_vertical, down case")
        # print('here is check_vertical result1: '+ str(affected_pieces))
        # print('result ' + str(result))
        return result


    def check_horizontal(self,coordinate_tuple,color):
        """
        return all pieces need to be flipped in this row (left and right)
        """
        result = []
        affected_pieces = []
        column_count = coordinate_tuple[1]
        opposite_color = self.get_opposite_color(color)
        #check the left side of the piece located at coordinate_tuple, hence the number column_count goes down
        while column_count > 0:
            # check the one on the left side of it, hence decrementing
            column_count -= 1
            if self.board[coordinate_tuple[0]][column_count] == color:
                if len(affected_pieces) > 0:
                    result.extend(affected_pieces)
                break
            elif self.board[coordinate_tuple[0]][column_count] == opposite_color:
                affected_pieces.append((coordinate_tuple[0], column_count))
                continue
            elif self.board[coordinate_tuple[0]][column_count] == Piece.VOID:
                #again generating an invalid move
                break
            else:
                raise NameError("Unexpected case at check_horizontal, left case")


        #check the right side of the piece located at coordinate_tuple, hence the number column_count goes up
        affected_pieces = []
        column_count = coordinate_tuple[1]
        while column_count < 7:
            # check the one on the left side of it, hence decrementing
            column_count += 1
            if self.board[coordinate_tuple[0]][column_count] == color:
                if len(affected_pieces) > 0:
                    result.extend(affected_pieces)
                break
            elif self.board[coordinate_tuple[0]][column_count] == opposite_color:
                affected_pieces.append((coordinate_tuple[0], column_count))
                continue
            elif self.board[coordinate_tuple[0]][column_count] == Piece.VOID:
                #again generating an invalid move
                break
            else:
                raise NameError("Unexpected case at check_horizontal, right case")
        # print(str(affected_pieces))
        # print('here is check_horizontal result: '+ str(affected_pieces))
        # print('here is check_horizontal result1: '+ str(result))
        return result


    def check_diagonal(self,coordinate_tuple,color):
        """
        See if that move will flip any pieces diagonally (two slash)
        """

        result = []
        affected_pieces = []
        opposite_color = self.get_opposite_color(color)

        # North West direction
        row = coordinate_tuple[0]
        column = coordinate_tuple[1]
        while row > 0 and column > 0:
            row -= 1
            column -= 1
            if self.board[row][column] == color:
                if len(affected_pieces) > 0:
                    result.extend(affected_pieces)
                break
            elif self.board[row][column] == opposite_color:
                affected_pieces.append((row, column))
                continue
            elif self.board[row][column] == Piece.VOID:
                #again generating an invalid move
                break
            else:
                raise NameError("Unexpected case at check_diagonal, N-W case")
        # print('affected_pieces ' + str(affected_pieces))
        # North East direction
        affected_pieces = []
        row = coordinate_tuple[0]
        column = coordinate_tuple[1]
        while row > 0 and column < 7:
            row -= 1
            column += 1
            if self.board[row][column] == color:
                if len(affected_pieces) > 0:
                    result.extend(affected_pieces)
                break
            elif self.board[row][column] == opposite_color:
                affected_pieces.append((row, column))
                continue
            elif self.board[row][column] == Piece.VOID:
                #again generating an invalid move
                break
            else:
                raise NameError("Unexpected case at check_diagonal, N-E case")

        # print('affected_pieces ' + str(affected_pieces))
        # South West direction
        affected_pieces = []
        row = coordinate_tuple[0]
        column = coordinate_tuple[1]
        while row < 7 and column > 0:
            row += 1
            column -= 1
            if self.board[row][column] == color:
                if len(affected_pieces) > 0:
                    result.extend(affected_pieces)
                break
            elif self.board[row][column] == opposite_color:
                affected_pieces.append((row, column))
                continue
            elif self.board[row][column] == Piece.VOID:
                #again generating an invalid move
                break
            else:
                raise NameError("Unexpected case at check_diagonal, S-W case")

        # print('affected_pieces ' + str(affected_pieces))
        # South Eest direction
        affected_pieces = []
        row = coordinate_tuple[0]
        column = coordinate_tuple[1]
        while row < 7 and column < 7:
            row += 1
            column += 1
            if self.board[row][column] == color:
                if len(affected_pieces) > 0:
                    result.extend(affected_pieces)
                break
            elif self.board[row][column] == opposite_color:
                affected_pieces.append((row, column))
                continue
            elif self.board[row][column] == Piece.VOID:
                #again generating an invalid move
                break
            else:
                raise NameError("Unexpected case at check_diagonal, S-W case")
        # print('here is check_digonal result: '+ str(affected_pieces))
        return result


    def get_opposite_color(self,color):
            if(color == Piece.BLACK):
                return Piece.WHITE
            elif(color == Piece.WHITE):
                return Piece.BLACK
            else:
                raise NameError("Wrong param to get_opposite color")

    #Useful I/O functions
    def return_pieces_count(self):
        """
        Return a dictionary : {Piece.BLACK: num, Piece.WHITE : num, Piece.VOID : num}
        """
        pieces_count = {}
        pieces_count[Piece.BLACK] = 0
        pieces_count[Piece.WHITE] = 0
        pieces_count[Piece.VOID] = 0

        for row in range(8):
            for column in range(8):
                if self.board[row][column] == Piece.BLACK:
                    pieces_count[Piece.BLACK] += 1
                elif self.board[row][column] == Piece.WHITE:
                    pieces_count[Piece.WHITE] += 1
                else:
                    pieces_count[Piece.VOID] += 1
        return pieces_count


    def get_winner(self):
        """
        Return the color that won
        Output : Piece.White
                 Piece.Black
                 Piece.TIE # if they tie
        """
        pieces_count = self.return_pieces_count()
        if pieces_count[Piece.BLACK] > pieces_count[Piece.WHITE]:
            return Piece.BLACK
        elif pieces_count[Piece.BLACK] == pieces_count[Piece.WHITE]:
            return Piece.TIE
        else:
            return Piece.WHITE

    def print_board(self):
        '''
        Print the board beautifully on terminal
        '''
        print("The board is:")
        print("  0 1 2 3 4 5 6 7")
        for row in range(8):
            print(row, end = " ")
            for column in range(8):
                if self.board[row][column] == Piece.VOID:
                    print(" ", end = " ")
                elif self.board[row][column] == Piece.BLACK:
                    print("*", end = " ")
                elif self.board[row][column] == Piece.WHITE:
                    print("o", end = " ")
            print("", end="\n")
        return

    def get_board(self):
        # Return the board object. In this case, each board can be represented as state
        return self.board



