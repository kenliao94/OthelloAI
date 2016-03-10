from config import *

#This class defines the Game object with collect some info about the game and bundle
#player objects, board object
class Game:
    def __init__(self,name,player1,player2,board):
        '''
        This function init the game object
        '''
        self.name = name
        self.player1 = player1
        self.player2 = player2
        self.board = board
        self.current_round = Player.FIRST

    def start(self):
        game_end = False
        while not game_end:
            self.board.print_broad()
            #First player move, can be either AI or human
            if self.current_round == Player.FIRST:
                #Player 1
                move = self.player1.thinking(self.board.get_board(),self.board.get_possible_move(self.player1.color))
                if move is None:
                    #That means there is no possible move, which can happen during the game
                    self.current_round = Player.SECOND
            else:
                #Player 2
                move = self.player2.thinking(self.board.get_board(),self.board.get_possible_move(self.player2.color))
                if move is None:
                    self.current_round = Player.SECOND

            #Check end game:
            if self.board.check_end_game():
                game_end = True

    def print_game_status(self):
        #print winner
        print(self.board.get_winner())
