from config import *

class AI:
    def __init__(self,color,responseTime,difficulty):
        self.color = color
        self.responseTime = responseTime
        self.difficulty = difficulty

    def thinking(self,board):
        #the board is useless, use standard I/O
        return ()

    # MUCH more internal routine to make things work