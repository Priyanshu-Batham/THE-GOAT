import random
R = [random.randrange(1, 7), random.randrange(1, 7), random.randrange(
    1, 7), random.randrange(1, 7), random.randrange(1, 7), random.randrange(1, 7)]
count = [0, 0, 0, 0, 0, 0]

goatColors = ["BLack", "Orange", "Purple", "Green", "Red", "White"]
playerInfo = []


def drawline():
    for i in range(0, 10):
        print("+---", end="")
    print("+\n")


while True:
    n = int(input("Number of players:"))
    if n > 6 or n <= 1:
        print("Max players allowed are 6 and Min 2")
        continue
    else:
        break
for i in range(0, n):
    print("Enter Player", i+1, "name:")
    name = input()
    print(name, "Has", goatColors[i], "Goat")
    query = [i+1, name, goatColors[i]]
    playerInfo.append(query)

# visual representation of the game board------------------------------>>>


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
    for f in playerInfo:
        for q in f:
            print("     ", q, end="      ")
        print("\n")


board()

# --------------------------STACK CLASS--------------------->>


class Stack():
    items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

'''
# testing the stack class
stack = Stack()
stack.push('hello')
print(stack.peek())
stack.push('priyanshu')
print(stack.pop())
print(stack.peek())
# Stack class working perfectly
'''

# --------------------------GOAT CLASS--------------------->>


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
        if (self.row == -1 and self.column == ''):
            return -1
        else:
            location = self.column + str(self.row)
            return location

    def setLocation(self, x, y):
        self.column = x
        self.row = y


# testing the goat class and object
'''
color = "white"
goat1 = Goat(color)
print(goat1.getColor())
print(goat1.getLocation())
goat1.setLocation('B', 5)
print(goat1.getLocation())
# goat class working smoothly
'''


class Player:
    def __init__(self, playernumber):
        self.playernumber = playernumber
        print(playerInfo[playernumber])
     #   print(I[playernumber[2]])


g = int(input("Enter player number:"))
o = Player(g)
print(o.playernumber)
