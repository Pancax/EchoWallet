class Instance:

    def __init__(self, timedata, mood):
        # use self when we set timeStamp
        self.timeStamp = timedata
        self.mood = mood["Happy"]*1
        self.mood = self.mood+mood["Angry"]*.5
        self.mood = self.mood+mood["Surprise"]*1
        self.mood = self.mood+mood["Sad"]*-.5
        self.mood = self.mood+mood["Fear"]*-1
        self.mood = (self.mood+1.5)/(2.5+1.5)
