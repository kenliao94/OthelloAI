def convert_board_to_string(board):
        '''
        :param board: a list
        :return: a string
        '''
        string = ""
        for i in range (8):
            for t in range(8):
                string += board[i][t]
        return string

def log_to_file(str,filename):
    '''it will log the string to particular file specify by filename'''
    f = open(filename,'a')
    f.write(str)
    f.close()
    return

