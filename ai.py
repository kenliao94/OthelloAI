from config import *
from gametree import *
from heuristic import *

class AI:
    def __init__(self,color,responseTime,difficulty):
        self.color = color
        self.responseTime = responseTime
        self.difficulty = difficulty

    def thinking(self,board,possible_move):
        if len(possible_move) == 0:
            return None
        else:
            current_node = Node(board,self.color)
            opponent = current_node.board.get_opposite_color(self.color)
            value = alphabeta_minimax(current_node,0,3,dummy_heur,current_node.curPlayer,current_node.curPlayer,opponent,-1000000,1000000)
            #The second element of the value tuple is which
            possible_move = current_node.board.get_possible_move(self.color)
            return possible_move[value[1]]

