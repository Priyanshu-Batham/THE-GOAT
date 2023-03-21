import random



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
    column = '-1'

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

# ----------------PLAYER CLASS---------------->>>>>


class Player(Goat):
    color = ''
    playerName = ''
    playerGoats = []
    def __init__(self, playerName, color):
        self.color = color
        self.playerName = playerName
        for i in range(0,4):
            obj = Goat(color)
            self.playerGoats.append(obj)

    def __str__(self) -> str:
        return f"Name: {self.playerName}\t Color: {self.color}\nGoat 1: {self.getGoat(0)}\nGoat 2: {self.getGoat(1)}\nGoat 3: {self.getGoat(2)}\nGoat 4: {self.getGoat(3)}"

    def addGoat(self):
        obj = Goat(self.color)
        self.playerGoats.append(obj)

    def removeGoat(self,num):
        self.playerGoats.pop(num)

    def playerColor(self):
        return self.color
    
    def goatCount(self):
        return len(self.playerGoats)
    
    def setGoat(self,num,column,row):
        self.playerGoats[num].setLocation(column,row)

    def getGoat(self,num):
        return self.playerGoats[num].getLocation()
# ------------------------------------------->>>>>>

R = [random.randrange(1, 7), random.randrange(1, 7), random.randrange(
    1, 7), random.randrange(1, 7), random.randrange(1, 7), random.randrange(1, 7)]
count = [0, 0, 0, 0, 0, 0]
goatColors = ["BLack", "Orange", "Purple", "Green", "Red", "White"]
players = []

# visual representation of the game board------------------------------>>>
def drawline():
    for i in range(0, 10):
        print("+---", end="")
    print("+\n")


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


board()
    

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
    print("\n",name, "Has", goatColors[i], "Goat\n")

    print("Enter 4 Goat Locations\n")
    goat1column = input()
    goat1row = int(input())

    goat2column = input()
    goat2row = int(input())

    goat3column = input()
    goat3row = int(input())

    goat4column = input()
    goat4row = int(input())

    playerObj = Player(name,goatColors[i])
    playerObj.setGoat(0,goat1column,goat1row)
    playerObj.setGoat(1,goat2column,goat2row)
    playerObj.setGoat(2,goat3column,goat3row)
    playerObj.setGoat(3,goat4column,goat4row)
    players.append(playerObj)


for i in range(0,n):
    print(players[i],"\n")

