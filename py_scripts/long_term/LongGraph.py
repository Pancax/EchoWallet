class LongGraph:

    def __init__(self, name):
        self.graphList = []
        self.name=name

    def addLongPoint(self, point):
        self.graphList.append(point)

    def makeGraphGood(self):
        self.graphList.sort(key=lambda x: x.time)