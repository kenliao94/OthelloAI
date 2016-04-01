from config import *
from copy import *

class node:
    def __init__(self,board,color):
        self.board = board
        self.max_player = color
        #essentially running the get opposite color function. Too lazy to port it here
        if color == Piece.BLACK:
            self.min_player = Piece.WHITE
        elif color == Piece.WHITE:
            self.min_player = Piece.BLACK
        else:
            raise NameError("Unexpected case at node class")

def minimax(node,current_level,search_limit,heur,player,max_player,min_player):
    #base cases for recursion, i.e check if depth limit is reached or the game is ended
        #Case 1 check if game is ended
    if node.board.check_end_game():
        winner = node.board.get_winner()
        if winner == Piece.TIE:
            return Constant.tie_value
        elif winner == node.max_player:
            return Constant.max_player_endgame_value
        elif winner == node.min_player:
            return Constant.min_player_endgame_value
        else:
            raise NameError("Unexpected case at minimax check phase")
    #check if the depth limit is reached
    if current_level >= search_limit:
        return heur(node.board,node,player)
    #general cases
    #refer to slides, also use deepcopy to create node
    score_array = []
    for possible_move in node.board.get_possible_move(player):
        new_node = deepcopy(node)
        new_node.board.make_move(possible_move,player)
        if player == max_player:
           score = minimax(new_node,current_level+1,search_limit,heur,min_player,max_player,min_player)
           score_array.append(score)
        elif player == min_player:
           score = minimax(new_node,current_level+1,search_limit,heur,max_player,max_player,min_player)
           score_array.append(score)
        else:
            raise NameError("Unexpected case at score")

    #calculate max or min value depending on player
    if player == max_player:
        return max(score_array)
    elif player == min_player:
        return  min(score_array)
    else:
        raise  NameError("Unexpected case at last in minimax")

def alphabeta_minimax(node,current_level,search_limit,heur,player,max_player,min_player,alpha,beta):
    #base cases for recursion, i.e check if depth limit is reached or the game is ended
        #Case 1 check if game is ended
    if node.board.check_end_game():
        winner = node.board.get_winner()
        if winner == Piece.TIE:
            return Constant.tie_value
        elif winner == node.max_player:
            return Constant.max_player_endgame_value
        elif winner == node.min_player:
            return Constant.min_player_endgame_value
        else:
            raise NameError("Unexpected case at minimax check phase")
    #check if the depth limit is reached
    if current_level >= search_limit:
        return heur(node.board,node,player)
    #general cases
    if player == max_player:
        for possible_move in node.board.get_possible_move(player):
            new_node = deepcopy(node)
            new_node.board.make_move(possible_move,player)
            alpha = max(alpha,alphabeta_minimax(new_node,current_level+1,search_limit,heur,min_player,max_player,min_player,alpha,beta))
            if beta <= alpha:
                break
        return alpha
    elif player == min_player:
        for possible_move in node.board.get_possible_move(player):
            new_node = deepcopy(node)
            new_node.board.make_move(possible_move,player)
            beta = min(beta,alphabeta_minimax(new_node,current_level+1,search_limit,heur,max_player,max_player,min_player,alpha,beta))
            if beta <= alpha:
                break
        return beta
    else:
        raise NameError("Unexpected case at minimax alpha beta")
    #LOOK At slides, not correctly implemented
