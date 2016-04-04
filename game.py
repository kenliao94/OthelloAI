from config import *


#This class defines the Game object with collect some info about the game and bundle
#player objects, board object
class Game:
    def __init__(self,name,player1,player2,board,collector):
        '''
        This function init the game object
        '''
        self.name = name
        self.player1 = player1
        self.player2 = player2
        self.board = board
        self.current_round = Player.FIRST
        self.collector = collector

    def start(self):
        game_end = False
        while not game_end:
            self.board.print_board()
            #First player move, can be either AI or human
            if self.current_round == Player.FIRST:
                print("Player 1's turn")
                #Collect number of steps
                self.collector.log_to_file(str(len(self.board.get_possible_move(self.player1.color))))
                #Player 1
                move = self.player1.thinking(self.board,self.board.get_possible_move(self.player1.color))
                if move is None:
                    #That means there is no possible move, which can happen during the game
                    #print("Changing player")
                    self.current_round = Player.SECOND
                else:
                    self.board.make_move(move,self.player1.color)
                    #print("Changing player case b")
                    self.current_round = Player.SECOND
            else:
                #Player 2
                print("Player 2's turn")
                self.collector.log_to_file(str(len(self.board.get_possible_move(self.player2.color))))
                move = self.player2.thinking(self.board,self.board.get_possible_move(self.player2.color))
                if move is None:
                    self.current_round = Player.FIRST
                else:
                    self.board.make_move(move,self.player2.color)
                    self.current_round = Player.FIRST

            #Check end game:
            if self.board.check_end_game():
                game_end = True

    def print_game_status(self):
        #print winner
        winner = self.board.get_winner()
        if winner == Piece.BLACK:
            print("Black wins")
        elif winner == Piece.WHITE:
            print("White wins")
        else:
            print("TIE")
        self.board.print_board()
        return
