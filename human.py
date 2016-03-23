from board import *
class Human:
    def __init__(self,color):
        self.color = color

    def thinking(self,board,possible_move):
        # print out hints
        #the board is useless, use standard I/O
        print(board)
        if len(possible_move) == 0:
            print('No legal move available for human. Computer will make a move.')
            return
        else:

            while(1):

                print('Here are all possible moves you could make: ' + str(possible_move))
                print('Please enter your move in row_number, column_number format(i.e. 1, 3): ', end='')
                human_move = input().replace(" ", "")

                if human_move.find(',') == -1:
                    print('You forget to put comma(,) between row number and column number ')
                    continue

                row = human_move.split(',')[0]
                column = human_move.split(',')[1]


                if len(human_move.split(',')) == 2 and row.isnumeric() and column.isnumeric() and (int(row),int(column)) in possible_move:
                    return (int(row),int(column))
                else:
                    print(board)
                    print('Your move is invalid')



a = Human('white')
b = Board()
c = a.thinking(b, [(1, 3), (2, 3)])
print(c)

