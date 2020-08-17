max_case_x=50
max_case_y=30
total_pop=500
tPropagation=30
tImmunity=10
tDeath=20
incubationTime=3
mortel=True
max_turn=10
confinement=False

case_list = []
pop_list = []
turn_list=[]

from case import Case
import randomCasePicking

def getCase(x, y):
    for i in case_list:
        case_location=i.getLocation()
        if case_location[0] == x:
            if case_location[1] == y:
                return i

def getPop(x, y):
    for i in pop_list:
        pop_location=i.getLocation()
        if pop_location[0] == x:
            if pop_location[1] == y:
                return i

def people_rarity():
    return True

import random
def generate_terrain(x, y):
    for j in range(y+1):
        for i in range(x+1):
            case=Case(False, i, j)
            if people_rarity():
                case.addPop()
                pop_list.append(getPop(case.getLocation[0], case.getLocation[1]))
            case_list.append(case)

def get_color_case(case):
    if case.hasPop():
        pop = getPop(case.getLocation[0], case.getLocation[1])
        if pop.isDead():
            return "grey"
        elif pop.isContaminated():
            return "red"
        else:
            return "green"
    else:
        return "white"

from turtle import Turtle as ttle
def print_turn(x, y):
    turtle.pensize(1)
    for j in range(y+1):
        for i in range(x+1):
            ttle.setx(i)
            turtle.right(1)


import case
import randomCasePicking
import pop
def start():
    generate_terrain(max_case_x, max_case_y)
    for current_turn in range(max_turn):
        for i in case_list:
            if i.hasPop() and not getPop(i.getLocation[0], i.getLocation[1]).isDead:
                if getPop(i.getLocation[0], i.getLocation[1]).isContaminated:
                    randomCasePicking.rVirusCasePicking(i.getLocation, tPropagation)
                pop = getPop(i.getLocation[0], i.getLocation[1])
                if pop.isContaminated:
                    pop.addContaminatedTurn
                    if pop.getContaminatedTime > incubationTime:
                        if random.randint(1,100) <= tDeath:
                            pop.die
                        elif random.randint(1,100) <= tImmunity:
                            pop.deContaminate
                            randomCasePicking.rPopCasePicking(i.getLocation)
                        else:
                            randomCasePicking.rPopCasePicking(i.getLocation)
                else:
                    randomCasePicking.rPopCasePicking(i.getLocation)

if __name__ == "__main__":
    start()