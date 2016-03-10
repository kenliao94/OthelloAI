from config import *
from gametree import *

class AI:
    def __init__(self,color,responseTime,difficulty):
        self.color = color
        self.responseTime = responseTime
        self.difficulty = difficulty

    def thinking(self,board,possible_move):
        return ()

    # MUCH more internal routine to make things work