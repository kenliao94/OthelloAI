from config import *
from gametree import *
from heuristic import *

class AI:
    def __init__(self,color,heur,steps_adv):
        self.color = color
        self.heur = heur
        self.steps_adv = steps_adv

    def thinking(self,board,possible_move):
        if len(possible_move) == 0:
            return None
        else:
            current_node = Node(board,self.color)
            opponent = current_node.board.get_opposite_color(self.color)

            value = alphabeta_minimax(current_node,0,self.steps_adv,self.heur,self.color,self.color,opponent,-1000000,1000000)
            #value = minimax(current_node,0,self.steps_adv,self.heur,self.color,self.color,opponent)
            possible_move = current_node.board.get_possible_move(self.color)
            return possible_move[value[1]]

