# This is the main control loop of the game. Consider wrapping this game in an object. Much better design
from human import *
from ai import *
from board import *
from game import *
from config import *
from collector import *
from logger import *

heurs_function = {1:heuristic_1, 2:heuristic_2,3:heuristic_3, 4:heuristic_4, 5:heuristic_5, 6:heuristic_6, 7:heuristic_7}
heurs_name = {1:"heuristic_1", 2:"heuristic_2",3:"heuristic_3", 4:"heuristic_4", 5:"heuristic_5", 6:"heuristic_6", 7:"heuristic_7"}
oneline = "-------------------------------------------------------"

first = 1

while first < 8:

    second = 1
    while second < 8:

        if first == second:
            second += 1
            continue
        print('-------------------------------new game------------------------------------')
        log_to_file("whowin: BLACK," + heurs_name[first]  + " VS WHITE," + heurs_name[second]  + "\n","test_new_heur_result.txt")

        black = 0
        white = 0
        tie = 0


        p1 = AI(Piece.BLACK,heurs_function[first],2)
        p2 = AI(Piece.WHITE,heurs_function[second],2)
        board = Board([])
        data_collector = Collector("data.out")
            #start the game
        game1 = Game("Game1",p1,p2,board,data_collector)
        game1.start()
        game1.print_game_status()

        winner = board.get_winner()
        if winner == Piece.BLACK:
            black += 1
        elif winner == Piece.WHITE:
            white += 1
        else:
            tie += 1

        log_to_file("\n","test_new_heur_result.txt")
        log_to_file('BLACK: ' + str(black),"test_new_heur_result.txt")
        log_to_file('WHITE: ' + str(white),"test_new_heur_result.txt")
        log_to_file('TIE: ' + str(tie),"test_new_heur_result.txt")
        log_to_file("\n\n\n" + oneline + "\n\n\n","test_new_heur_result.txt")
        second += 1
    first += 1
#-----------------------------------------------------------------------------------------------------


