import random


def rPopCasePicking(caseLocation):
    rInt = random.randint(1, 4)
    if rInt == 1:
        getCase(caseLocation[0], caseLocation[1]+1).addPop()

        elif rInt == 2:
            getCase(caseLocation[0]+1, caseLocation[1]).addPop()
            elif rInt == 3:
                getCase(caseLocation[0], caseLocation[1]-1).addPop()
                elif rInt == 4:
                    getCase(caseLocation[0]-1, caseLocation[1]).addPop()
    getCase(caseLocation[0], caseLocation[1]).removePop

def rVirusCasePicking(caseLocation, tPropagation):
    adjCase1 = getCase(caseLocation[0], caseLocation[1]+1)
    adjCase2 = getCase(caseLocation[0]+1, caseLocation[1])
    adjCase3 = getCase(caseLocation[0], caseLocation[1]-1)
    adjCase4 = getCase(caseLocation[0]-1, caseLocation[1])
    adjCaseList = [adjCase1, adjCase2, adjCase3, adjCase4]
    for i in range(len(adjCaseList)):
        if random.randint(1, 100) <= tPropagation:
            if i.hasPop:
                getPop(i.getLocation[0], i.getLocation[1]).contaminate

    