def convert_board_to_string(board):
        '''
        :param board: a list
        :return: a string
        '''
        string = ""
        for i in range (8):
            for t in range(8):
                string += str(board[i][t])
        return string

def log_to_file(str,filename):
    '''it will log the string to particular file specify by filename'''
    str += "\n"
    f = open(filename,'a')
    f.write(str)
    f.close()
    return

def convert_string_to_board(str):
    '''Opposite of convert_board_to_string'''
    board = []
    for i in range(8):
        temp = []
        for t in range(8):
            temp.append(int(str[ i * 8 + t]))
        board.append(temp)
    return board
