# represents one data point on our list of datas.
from data_generate.short_term.Instance import Instance


class Ticker:

    def __init__(self, name):
        # use self when we set timeStamp
        self.name = name
        self.comCount = 0
        self.aggTime = 0
        self.list = []
        self.finalX = 0.0
        self.aggMood= 0.0
        self.finalZ = 0.0

    def add_instance(self, timestamp, mood):
        guy = Instance(timestamp,mood)
        self.list.append(guy)
        self.aggTime = (self.aggTime + guy.timeStamp)
        self.finalX = self.aggTime / len(self.list)
        self.aggMood = guy.mood+self.aggMood
        self.finalZ = self.aggMood/len(self.list)

    def add_comment(self):
        self.comCount+=1