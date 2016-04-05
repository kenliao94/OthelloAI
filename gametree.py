from config import *
from copy import *
from logger import *

class Node:
    def __init__(self,board,color):
        self.board = board
        # self.max_player = color
        # #essentially running the get opposite color function. Too lazy to port it here
        # if color == Piece.BLACK:
        #     self.min_player = Piece.WHITE
        # elif color == Piece.WHITE:
        #     self.min_player = Piece.BLACK
        # else:
        #     raise NameError("Unexpected case at node class")
        self.curPlayer = color

def minimax(node,current_level,search_limit,heur,player,max_player,min_player):
    #base cases for recursion, i.e check if depth limit is reached or the game is ended
        #Case 1 check if game is ended
    #print("-----------------------------------------------")#NO_PRINT
    #print("Running at level {}".format(current_level))#NO_PRINT
    if node.board.check_end_game():
        winner = node.board.get_winner()
        if winner == Piece.TIE:
       #     print("End State reached : TIE") #NO_PRINT
            return Constant.tie_value,0
        elif winner == max_player:
       #     print("End State reached : Max Player Win") #NO_PRINT
            return Constant.max_player_endgame_value,0
        elif winner == min_player:
       #     print("End State reached : Min Player Win") #NO_PRINT
            return Constant.min_player_endgame_value,0
        else:
            raise NameError("Unexpected case at minimax check phase")
    #check if the depth limit is reached
    if current_level >= search_limit:
        heur_val = heur(node.board,max_player)
        #print("Reach limit level, return heuristic : {}".format(heur_val)) #NO_PRINT
        #print("-----------------------------------------------------") #NO_PRINT
        return heur_val,0
    #general cases
    #refer to slides, also use deepcopy to create node
    possible_move_list = node.board.get_possible_move(player)

    if len(possible_move_list) == 0:
        if player == max_player:
            new_node = deepcopy(node)
            opponent = new_node.board.get_opposite_color(player)
            new_node.curPlayer = opponent
            score = minimax(new_node,current_level+1,search_limit,heur,min_player,max_player,min_player)
            return score[0],0

        elif player == min_player:
            new_node = deepcopy(node)
            opponent = new_node.board.get_opposite_color(player)
            new_node.curPlayer = opponent
            score = minimax(new_node,current_level+1,search_limit,heur,max_player,max_player,min_player)
            return score[0],0

    else:
        score_array = []
        for possible_move in node.board.get_possible_move(player):
            new_node = deepcopy(node)
            #print_gametree_node_state(new_node) #NO_PRINT
            #Set the new_node current player to opposite color
            opponent = new_node.board.get_opposite_color(player)
            new_node.curPlayer = opponent

            new_node.board.make_move(possible_move,player)
           # print("Trying to make move : {}".format(possible_move)) #NO_PRINT
           # print("After move :") #NO_PRINT
           # print_gametree_node_state(new_node) #NO_PRINT
            if player == max_player:
               score = minimax(new_node,current_level+1,search_limit,heur,min_player,max_player,min_player)
               score_array.append(score[0])
            elif player == min_player:
               score = minimax(new_node,current_level+1,search_limit,heur,max_player,max_player,min_player)
               score_array.append(score[0])
            else:
                raise NameError("Unexpected case at score")

        #calculate max or min value depending on player
        index = 0
        #print(score_array)
        if player == max_player:
            #log_to_file(str(score_array),"data.out")
            max_score = max(score_array)
            for i in range(len(score_array)):
                if max_score == score_array[i]:
                    index = i
            return max_score,index
        elif player == min_player:
            #log_to_file(str(score_array),"data.out")
            min_score = min(score_array)
            for i in range(len(score_array)):
                if min_score == score_array[i]:
                    index = i
            return min_score,index
        else:
            raise  NameError("Unexpected case at last in minimax")

def alphabeta_minimax(node,current_level,search_limit,heur,player,max_player,min_player,alpha,beta):
    #base cases for recursion, i.e check if depth limit is reached or the game is ended
    #Case 1 check if game is ended
    # print("current_level:{}".format(current_level))
    # print("search_limit:{}".format(search_limit))
    # print("player:{}".format(player))
    # print("max player:{}".format(max_player))
    # print("min player:{}".format(min_player))
    if node.board.check_end_game():
        winner = node.board.get_winner()
        if winner == Piece.TIE:
            return Constant.tie_value,0
        elif winner == max_player:
            return Constant.max_player_endgame_value,0
        elif winner == min_player:
            return Constant.min_player_endgame_value,0
        else:
            raise NameError("Unexpected case at minimax check phase")
    #check if the depth limit is reached
    if current_level >= search_limit:
        return heur(node.board,max_player),0
    #general cases
    index = 0
    desire_index = 0

    possible_move_list = node.board.get_possible_move(player)
    if len(possible_move_list) == 0:
        if player == max_player:
            new_node = deepcopy(node)
            opponent = new_node.board.get_opposite_color(player)
            new_node.curPlayer = opponent
            return_from_minimax = alphabeta_minimax(new_node,current_level+1,search_limit,heur,min_player,max_player,min_player,alpha,beta)
            return return_from_minimax[0],0
        elif player == min_player:
            new_node = deepcopy(node)
            opponent = new_node.board.get_opposite_color(player)
            new_node.curPlayer = opponent
            return_from_minimax = alphabeta_minimax(new_node,current_level+1,search_limit,heur,max_player,max_player,min_player,alpha,beta)
            return return_from_minimax[0],0
        else:
            raise NameError("Unexpected case at minimax alpha beta")

    else:
        if player == max_player:
            for possible_move in node.board.get_possible_move(player):
                new_node = deepcopy(node)
                new_node.board.make_move(possible_move,player)
                opponent = new_node.board.get_opposite_color(player)
                new_node.curPlayer = opponent
                #print_gametree_node_state(new_node) #NO_PRINT
                #notice, directly calling aphabeta_minimax will return a tuple, hence need that [0]
                return_from_minimax = alphabeta_minimax(new_node,current_level+1,search_limit,heur,min_player,max_player,min_player,alpha,beta)
                alpha = max(alpha,return_from_minimax[0])
                if alpha == return_from_minimax[0]:
                    #that means the new alpha value replaced old one
                    desire_index = index
                index += 1
                if beta <= alpha:
                    break
            #Return the coordinate that has the highest utility value
            return alpha,desire_index

        elif player == min_player:
            for possible_move in node.board.get_possible_move(player):
                new_node = deepcopy(node)
                new_node.board.make_move(possible_move,player)
                opponent = new_node.board.get_opposite_color(player)
                new_node.curPlayer = opponent
                #notice, directly calling aphabeta_minimax will return a tuple, hence need that [0]
                return_from_minimax = alphabeta_minimax(new_node,current_level+1,search_limit,heur,max_player,max_player,min_player,alpha,beta)
                beta = min(beta,return_from_minimax[0])
                if beta == return_from_minimax[0]:
                    desire_index = index
                index += 1
                if beta <= alpha:
                    break
            return beta,desire_index
        else:
            raise NameError("Unexpected case at minimax alpha beta")
