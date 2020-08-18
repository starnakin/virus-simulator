class Pop():
    def __init__(self, X, Y):
        self.location = [X, Y]
        self.isContaminate = False
        self.dead = False
        self.contaminatedTurn = 0

    def getLocation(self):
        return self.location

    def getContaminatedTurn(self):
        return self.contaminatedTurn

    def addContaminatedTurn(self):
        contaminatedTurn+1

    def isContaminated(self):
        return self.isContaminate

    def isDead(self):
        return self.dead

    def contaminate(self):
        self.isContaminate = True

    def deContaminate(self):
        self.isContaminate = False

    def die(self):
        self.isDead = True
