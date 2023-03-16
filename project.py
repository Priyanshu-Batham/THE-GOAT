import random
R=[random.randrange(1,7),random.randrange(1,7),random.randrange(1,7),random.randrange(1,7),random.randrange(1,7),random.randrange(1,7)] 
count=[0,0,0,0,0,0]

def drawline():
    for i in range(0,10):
        print("+---",end="")
    print("+\n")
I=[]
while True:
    n=int(input("Number of players:"))
    if n>6 or n<=1:
        print("Max players allowed are 6 and Min 2")
        continue
    else:
        break
L=["BLack","Orange","Purple","Green","Red","White"]
for i in range(0,n):
    print("Enter Player",i+1,"name:")
    d=input()
    print(d,"Has",L[i],"Goat")
    t=(i+1,d,L[i])
    I.append(t)

def board():
    print("Start",end=" ")
    for j in range(65,73):
        print(chr(j),end="   ")
    print("End")
    print("\n")
    for i in range(0,6):
        drawline()
        print (i+1,end="   ")
        for r in range(0,10):
            print("|",end="")
            if R[i]==r:
                print(" X ",end="")
            else:
                print(end="   ")
        print("\n")
    drawline()
    print("Player Number | Player Name | Goat Colour")
    for f in I:
        for q in f:
            print("     ",q,end="      ")
        print("\n")
board()
        
    