#we define the board object here
from config import *

class board:

    def __init__(self):
        '''
        This function should create the board, in this case, it is represented as a 2D array with
        starter position. The board size is defined in config.py
        '''
        self.board = []
        return

    def check_end_game(self):
        '''
        This function is called to see if the board is filled
        '''
        return True

    def make_move(self,coordinate_tuple,color):
        '''
        :param coordinate_tuple: (x,y), (0,0) is top left corner
        :param color: the piece ENUM
        :return: true if move is valid, false if not
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
        return self.board



