from random import *

#For the circle
position_x = 250
position_y = 250

direction_x = 3
direction_y = 3

#For the rectangle
pos_rectx = 200
pos_recty = 460


def setup():
    size (500, 500)

#This is for the action performed when a key is pressed
def keyPressed():
    print("pressed %s %d" % (key, keyCode))
    if keyPressed == 37:
        pos_rectx +=1
    if keyPressed == 39:
        pos_rectx -=1
    
    
    
    
    
def draw():
        global position_x
        global position_y
        global direction_x
        global direction_y
        global pos_rectx
        global pos_recty
        
        background(0);
        
        #This is the code for the circle
        fill(0, 255, 255)
        ellipse (position_x, position_y, 45, 45)
        
        #This code is for the rectangle
        fill(255, 0, 10)
        rect(pos_rectx, pos_recty, 100, 20)
        position_x += direction_x
        position_y += direction_y
        if position_x == 475:   #This is for the right side of the screen
            direction_x *= -1
        if position_x == 25:    #This is for the left side of the screen
            direction_x *= -1
        if position_y == 25:    #This is for the top side of the screen
            direction_y *= -1   #I erased the bottom side for game over to be possible
            
            
    #This is for the paddle to make the ball bounce off it
        if position_y  == pos_recty + 20:
            if pos_rectx  < position_x < pos_rectx + 100:
                print(position_y)
                print(pos_recty)
                direction_y *= -1 


            
#This is for the action performed when a key is pressed
def keyPressed():
    global pos_rectx
    global pos_recty
    global position_x
    global position_y
    global direction_x
    global direction_y
    global pos_rectx
    global pos_recty
    print("pressed %s %d" % (key, keyCode))
    if keyCode == 39 and pos_rectx + 100 < 500:
        pos_rectx +=10
    if keyCode == 37 and pos_rectx > 0:
        pos_rectx -=10
'''       
#This is for the paddle to make the ball bounce off it
    if pos_rectx  == position_x:
        direction_x *= -1 
'''

            
        

        
        
        
        

            
    
        
        