from random import *

def setup():
    size (500, 500)
    

def draw():
    stroke(randrange(0,255), randrange(0,255), randrange(0,255))
    line(mouseX, mouseY, 250, 250)
    