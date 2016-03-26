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

            This code should change the board based on that move, i.e if I call Board.make_move(3,5), then the white piece at (3,4) will change

            Output : 1 if succeeded, 0 if failed
        '''
        return True

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
                    if self.check_vertical((row,column),color):
                        possible_move.append((row,column))
                        continue
                    if self.check_horizontal((row,column),color):
                        possible_move.append((row,column))
                        continue
                    if self.check_diagonal((row,column),color):
                        possible_move.append((row,column))

        return possible_move

    #End Game
    def check_end_game(self):
        '''
        This function is called to see if the board is filled
        Example :
            Input : None
            Output : true if it is ended, false if not

            Cases :
            1. The board is filled
            2. There is only one color (i.e, even the board is not filled, there is a possiblity that black gets wiped out, hence white wins)

        '''
        return True

    #Internal routine for make_move,
    def check_vertical(self,coordinate_tuple,color):
        '''
        See if that move will flip any pieces vertically (up and down)
        '''
        #Check Up
        up_count = coordinate_tuple[1]
        found_opposite_color = False
        opposite_color = self.get_opposite_color(color)
        #the up is looking up the board, hence the number goes down
        while up_count > 0:
            # check the one above it, hence decrementing
            up_count = up_count - 1
            if self.board[coordinate_tuple[0]][up_count] == color and not found_opposite_color:
                #that means the color is the same, generating an invalid move in the upward direction
                break
            elif self.board[coordinate_tuple[0]][up_count] == color and found_opposite_color:
                #found a valid move
                return True
            elif self.board[coordinate_tuple[0]][up_count] == opposite_color:
                found_opposite_color = True
                #keep checking
                continue
            elif self.board[coordinate_tuple[0]][up_count] == Piece.VOID:
                #again generating an invalid move
                break
            else:
                raise NameError("Unexpected case at check_vertical, up case")

        up_count = coordinate_tuple[1]
        found_opposite_color = False
        opposite_color = self.get_opposite_color(color)
        #check down
        # The down is looking down the board, hence number goes up
        while up_count < 7:
            # check the one above it, hence decrementing
            up_count = up_count + 1
            if self.board[coordinate_tuple[0]][up_count] == color and not found_opposite_color:
                #that means the color is the same, generating an invalid move in the upward direction
                break
            elif self.board[coordinate_tuple[0]][up_count] == color and found_opposite_color:
                #found a valid move
                return True
            elif self.board[coordinate_tuple[0]][up_count] == opposite_color:
                found_opposite_color = True
                #keep checking
                continue
            elif self.board[coordinate_tuple[0]][up_count] == Piece.VOID:
                #again generating an invalid move
                break
            else:
                raise NameError("Unexpected case at check_vertical, down case")

        #No valid move is found, return false 
        return False

    def check_horizontal(self,coordinate_tuple,color):
        '''
        See if that move will flip any pieces horizontal (left and right)
        '''
        return True

    def check_diagonal(self,coordinate_tuple,color):
        '''
        See if that move will flip any pieces diagonally (two slash)
        '''
        return True

    def get_opposite_color(self,color):
            if(color == Piece.BLACK):
                return Piece.WHITE
            elif(color == Piece.WHITE):
                return Piece.BLACK
            else:
                raise NameError("Wrong param to get_opposite color")

    #Useful I/O functions
    def return_pieces_count(self):
        '''
        Return a dictionary : {Piece.BLACK: num, Piece.WHITE : num, Piece.VOID : num}
        '''
        return {}

    def get_winner(self):
        '''
        Return the color that won
        Output : Piece.White
                 Piece.Black
                 Piece.TIE # if they tie
        '''
        return Piece.BLACK

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



