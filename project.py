import random

R = [random.randrange(1, 7), random.randrange(1, 7), random.randrange(
    1, 7), random.randrange(1, 7), random.randrange(1, 7), random.randrange(1, 7)]
count = [0, 0, 0, 0, 0, 0]


def drawline():
    for i in range(0, 10):
        print("+---", end="")
    print("+\n")


I = []
while True:
    n = int(input("Number of players:"))
    if n > 6 or n <= 1:
        print("Max players allowed are 6 and Min 2")
    else:
        break
L = ["BLack", "Orange", "Purple", "Green", "Red", "White"]
for i in range(0, n):
    print("Enter Player", i+1, "name:")
    d = input()
    print(d, "Has", L[i], "Goat")
    t = (i+1, d, L[i])
    I.append(t)


def board():
    print("Start", end=" ")
    for j in range(65, 73):
        print(chr(j), end="   ")
    print("End")
    print("\n")
    for i in range(0, 6):
        drawline()
        print(i+1, end="   ")
        for r in range(0, 10):
            print("|", end="")
            if R[i] == r:
                print(" X ", end="")
            else:
                print(end="   ")
        print("\n")
    drawline()
    print("Player Number | Player Name | Goat Colour")
    for f in I:
        for q in f:
            print("     ", q, end="      ")
        print("\n")


board()

# -----------------------------------------------GOAT CLASS---------------------------------------------->>
class Goat:
    color = ""
    row = -1
    column = ''
    
    # setting the color
    def __init__(self, goatColor):
        self.color = goatColor

    def getColor(self):
        return self.color

    def getLocation(self):
        if(self.row == -1 and self.column == ''):
            return -1
        else:
            location = self.column + str(self.row)
            return location

    def setLocation(self,x,y):
        self.column = x
        self.row = y

# testing the goat class and object 
color = "white"
goat1 = Goat(color)
print(goat1.getColor())
print(goat1.getLocation())
goat1.setLocation('B',5)
print(goat1.getLocation())
# goat class working smoothly

