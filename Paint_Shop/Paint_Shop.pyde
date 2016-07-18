def setup(): 
    size(400, 500)
    
    
color_choice = 1 
    
def draw():
    global color_choice
    noStroke()
    space = rect (0, 0, 400, 500 )
    
    
    fill(255, 255, 0)
    yellow_box = rect(0, 0, 50, 50)
    
    fill(255, 0, 0)
    red_box = rect(50, 0, 50, 50)
    
    fill(0, 0, 0)
    black_box = rect(100, 0, 50, 50)
    
    fill(255, 20, 147)
    pink_box = rect(150, 0, 50, 50)
    
    fill(0, 0, 255)
    blue_box = rect(200, 0, 50, 50)
    
    fill(0, 255, 0)
    green_box = rect(250, 0, 50, 50)
    
    fill(0, 255, 255)
    teal_box = rect(300, 0, 50, 50)
    
    fill(255, 255, 255)
    white_box = rect(350, 0, 50, 50)
    
    if mouseButton == LEFT:
        if mouseY < 50:
            if mouseX <50:
                color_choice = 1
            elif mouseX  <100:
                color_choice = 2
            elif mouseX <150:
                color_choice = 3
            elif mouseX < 200:
                color_choice = 4
            elif mouseX < 250:
                color_choice = 5
            elif mouseX < 300: 
                color_choice = 6
            elif mouseX < 350:
                color_choice = 7
        else: 
            print ("draw ellipse, color =", color_choice)
            if color_choice == 1:
                noStroke()
                fill(255, 0, 0)
                ellipse (mouseX, mouseY, 7, 7)
                
                
            
                
                
                
    
    

    
    
    

    