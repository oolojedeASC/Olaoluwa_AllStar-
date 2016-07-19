from random import *


position_x = randrange(10, 500)
position_y = randrange(10, 500)

direction_x = 1
direction_y = 1


def setup():
    size (500, 500)
    
def draw():
        global position_x
        global position_y
        global direction_x
        global direction_y
        
        background(20, 255, 0);
        fill(0, 255, 255)
        ellipse (position_x, position_y, 45, 45)
        position_x += direction_x
        position_y += direction_y
        if position_x == 475:
            direction_x *= -1
        if position_y == 475: 
            direction_y *= -1
        if position_x == 25:
            direction_x *= -1
        if position_y == 25:
            direction_y *= -1
            

        
        
        
        

            
    
        
        