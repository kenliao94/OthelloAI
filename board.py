#we define the board object here
from config import *

class Board:

    def __init__(self,board = []):
        '''
        This function should create the board, in this case, it is represented as a 2D array with
        starter position. The board size is defined in config.py
        '''
        self.board = board
        return


    def make_move(self,coordinate_tuple,color):
        '''
        It will make a move and change the board accordingly. The color is the current player
        '''
        return True

    def get_possible_move(self,color):
        '''
        Return a list of coordinate_tuple that the current player (with color) can play. If not possible then empty
        '''
        return []

    #End Game
    def check_end_game(self):
        '''
        This function is called to see if the board is filled
        '''
        return True

    #Internal routine for make_move,
    def check_vertical(self,coordinate_tuple,color):
        '''
        See if that move will flip any pieces vertically (up and down)
        '''
        return True

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

    #Useful I/O functions
    def return_pieces_count(self):
        '''
        Return a dictionary : {Piece.BLACK: num, Piece.WHITE : num, Piece.VOID : num}
        '''
        return {}

    def get_winner(self):
        '''
        Return the color that won
        '''
        return Piece.BLACK

    def print_broad(self):
        '''
        Print the board beautifully on terminal
        '''
        return

    def get_board(self):
        # Return the board object. In this case, each board can be represented as state
        return self.board



