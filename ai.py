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
            # value = alphabeta_minimax(current_node,0,self.steps_adv,self.heur,self.color,self.color,opponent,-1000000,1000000)
            # #value = minimax(current_node,0,self.steps_adv,self.heur,self.color,self.color,opponent)
            # possible_move = current_node.board.get_possible_move(self.color)


            #Another thinking algorithm
            score_array = []
            possible_move_list = current_node.board.get_possible_move(self.color)
            for possible_move in possible_move_list:
                new_node = deepcopy(current_node)
                #improvement !! Use alpha beta here
                new_node.board.make_move(possible_move,self.color)
                score = alphabeta_minimax(new_node,0,self.steps_adv,self.heur,opponent,self.color,opponent,-1000000,1000000)
                score_array.append(score[0])
            val = max(score_array)
            index = score_array.index(val)
            return possible_move_list[index]

