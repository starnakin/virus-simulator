max_case_x=50
max_case_y=30
total_pop=500
taux_contamination=1/4
mortel=True
max_turn=10
confinement=False

case_list = []
pop_list = []
turn_list=[]

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

import random
def generate_terrain(x, y):
    for j in range(y+1):
        for i in range(x+1):
            case=Case(i, j)
            if random.randint(0, total_pop/(max_case_x*max_case_y)):
                case.addPop()
                pop_list.append(Pop(i, j))
            case_list.append(case)

def get_color_case(pop):
    if pop.isDead():
        return "grey"
    elif pop.isContaminated():
        return "red"
    else:
        return "green"

import turtle
def print_turn(x, y):
    turtle.pensize(1)
    for j in range(y+1):
        for i in range(x+1):
            turtle.right(1)
            

def start():
    generate_terrain(max_case_x, max_case_y)
    for current_turn in range(max_turn):
        #contamination
        for i in case_list:
            if i.hasPop():
                i.test_virus()
        #déplacement
        for i in pop_list:
            i.move()
        turn_list.append(case_list)
        turn_list.append(pop_list)

if __name__ == "__main__":
    start()