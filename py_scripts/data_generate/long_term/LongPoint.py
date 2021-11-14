class LongPoint:

    def __init__(self, timedata):
        self.time = timedata
        self.count = 0.0

    def addCount(self,num):
        self.count+=num