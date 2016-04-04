import time

class Collector:
    #useful method for data collection
    def __init__(self,filename):
        self.filename = filename
        self.left_time = 0
        self.right_time = 0
        self.time_elapse = 0

    def start_timer(self):
        self.left_time = time.time()
        return

    def end_timer(self):
        self.right_time = time.time()
        time_elapse = self.right_time - self.left_time
        return time_elapse

    def log_to_file(self,str):
        str += "\n"
        f = open(self.filename,'a')
        f.write(str)
        f.close()
        return

