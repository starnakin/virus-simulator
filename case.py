class Case():
    def __init__(self, has_pop, X, Y):
        self.has_pop = has_pop
        self.location = [X, Y]

    def getLocation(self):
        return self.location

    def hasPop(self):
        return self.has_pop

    def addPop(self):
        self.has_pop = True

    def removePop(self):
        self.has_pop = False


