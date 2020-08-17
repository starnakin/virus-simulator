class Pop():
    def __init__(self, X, Y):
        self.location = [X, Y]
        self.isContaminate = False
        self.isDead = False
    
    def isContaminate(self):
        return self.isContaminate

    def isDead(self):
        return self.isDead
    
    def contaminate(self):
        self.isContaminate = True

    def deContaminate(self):
        self.isContaminate = False

    def die(self):
        self.isDead = True
