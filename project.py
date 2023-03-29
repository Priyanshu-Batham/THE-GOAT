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



# --------------------------GOAT CLASS--------------------->>


class Goat:
    color = ""
    row = -1
    column = '-1'

    # setting the color
    def _init_(self, goatColor):
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
    def _init_(self, playerName, color):
        self.color = color
        self.playerName = playerName
        for i in range(0,4):
            obj = Goat(color)
            self.playerGoats.append(obj)

    def _str_(self) -> str:
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
#count = [0, 0, 0, 0, 0, 0]
goatColors = ["Black", "Orange", "Purple", "Green", "Red", "White"]
players = []
G=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
count=[0,0,0,0,0,0]
flag=0
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
                ct = 0
                for z in range(0,4):
                    if r > 0 and r==G[i][z]:
                        print("",goatColors[i][0],z,end="")
                        ct = ct+1
                if(ct == 0):
                    print(end="   ")
                r+= ct
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
    players.append(name)
    print("\n",name, "Has", goatColors[i], "Goat\n")
    

for i in range(0,n):
    print(players[i],"\n")

#Starting the game
while True:
    if (count[0]==4):
        print(players[0],"Wins the game")
        break
           
    if count[1]==4:
        print(players[1],"Wins the game")
        break
    if count[2]==4:
        print(players[2],"Wins the game")
        break

    if (count[3]==4):
        print(players[3],"Wins the game")
        break
    if count[4]==4:
        print(players[4],"Wins the game")
        break

    if count[5]==4:
        print(players[5],"Wins the game")
        break
    

    for i in range(0,n):
         print(players[i],"'s turn")
         print("Enter to roll the dice:")
         l=input()
         dice=random.randrange(1,7)
         print("Dice showed ",dice)
  
         
         while True:
             d=int(input("Enter which number goat do you want to move 1:4="))
             if d>4 or d<1:
                 print("Invalid choice")
             elif G[i][d-1]>=8:
                 print("This goat is already at the end")
                 if G[0]==[8,8,8,8]:
                     break
                 if G[1]==[8,8,8,8]:
                     break
                 if G[2]==[8,8,8,8]:
                     break
                 if G[3]==[8,8,8,8]:
                     break
                 if G[4]==[8,8,8,8]:
                     break
                 if G[5]==[8,8,8,8]:
                     break
                 
             
             else:
                 G[i][d-1] = G[i][d-1]+dice
                 break
             if flag==1:
                 break
                 
             
      
         if G[i][d-1]>=8:
             G[i][d-1]=8
             count[i]=count[i]+1
             print(players[i],"'s",count[i],"goat reached final spot")
         
         print(players[i],"goat's postion:")
         board()
         for e in G[i]:
             print(chr(65+e),i+1,goatColors[i])