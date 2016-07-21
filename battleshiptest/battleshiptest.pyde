from random import *


board = [["0","0","0","0","0"],
         ["0","0","0","0","0"],
         ["0","0","0","0","0"],
         ["0","0","0","0","0"],
         ["0","0","0","0","0"]]

 #This picks a rectangle for the ship at random
board[(int(randrange(4)))][(int(randrange(4)))] = "Ship"


#This create the grid 
def setup():
    global board
    size(500, 500)
    for r in range(len(board)):
        for e in range(len(board)):
            rect(r*100, e*100, 100, 100)
            
#This performs an action when the left side of the mouse is clicked
def draw():
    global mPosx
    global mPosy
    
def mousePressed(): 
    global mPosx
    global mPosy
    mPosx = int(mouseX/100)
    mPosy = int(mouseY/100)
    if mouseButton == LEFT:
        if board[mPosx][mPosy] == "Ship":
            fill(76, 90, 200)
            rect(mPosx *100, mPosy*100, 100, 100)
            fill(25, 40, 89)
            text("Good job, soilder, you made America proud", 30, 30)
        else:
            fill(0)
            text("What are you doing soilder, you missed! Press 'r' to restart", 30, 30)
            
    