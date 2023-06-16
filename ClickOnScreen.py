#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 21:21:31 2021

@author: robertlino
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on WHAT DAY IS IT?

@author: Robert Lino

WHAT DOES YOUR GAME DO?
    OBJECTIVE - object not colliding
    RULES - up key increases speed, left key turns left, right key turns right
    CHALLENGE - navigating the turtle to touch one of the objects
    INTERACTIONS - reaction time

"""

import turtle
import time, random, math

# ================ LIBRARY SETTINGS SETUP =========================
turtle.colormode(255) # accept 0-255 RGB values
turtle.tracer(0) # turn off turtle's animation

panel = turtle.Screen()
w = 800
h = 800
panel.setup(width=w, height=h)
panel.bgcolor("yellowgreen")
#set up images for game


# ================ VARIABLE DEFINITION & SETUP =========================
running = True

# ================ FUNCTION DEFINITION =========================
# functions should go here IF they work with objects. 

def isCollision(t1,t2):
    """This function stops the objects from colliding using pythograus theorem
    t1=turtle1 and t2 = turtle2
    """
    a = t1.xcor()-t2.xcor() # t1 = turtle1 and t2=turtle2
    b = t1.ycor()-t2.ycor()
    distance = math.sqrt((a**2)+(b**2)) # Calculating distance using pythograus theorem ( http://analyticuniversity.com/)
    if distance <20:
        return True
    else:
        return False
# otherwise, try to include them in classes 

# ================ CLASSES =========================

class Player(turtle.Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("arrow")
        self.color("blue")
        self.speed = 1
        
    def move(self):
        self.forward(self.speed)
        
        if self.xcor()>300 or self.xcor() < -300: #this checks the boundaries
            self.left(60)
        if self.ycor()>300 or self.ycor() <-300:
            self.left(60)
    
   
        
          
    def turnleft(self):
        '''It makes the object turn left using the left key of the keyboard'''
        self.left(45)
    def turnRight(self):
        '''It makes the object turn right using the right key of the keyboard'''
        self.right(45)
    def speedUp(self):
        '''It increases the speed of the object when the up key on the keyboard is press'''
        self.speed += 1 # check and adds one to the current speed by pushing the up key

class Target(turtle.Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("red")
        self.speed = 1
        self.goto(random.randint(-275,275), random.randint(-275,275))
        self.setheading(random.randint(0,360))
    def jump(self):
        self.goto(random.randint(-275,275), random.randint(-275,275))
        self.setheading(random.randint(0,360))
    def move(self):
        self.forward(self.speed)
        #this checks the boundaries
        if self.xcor()>300 or self.xcor() < -300:
            self.left(60)
        if self.ycor()>300 or self.ycor() <-300:
            self.left(60)
def run():
    #classs instance
    player = Player()
    
    # create multiple targets
    targets = []
    for count in range (4):
        targets.append(Target())
        
        
    #Keyborad setup
    
    turtle.listen()
    turtle.onkey(player.turnleft, "Left")
    turtle.onkey(player.turnRight, "Right")
    turtle.onkey(player.speedUp,"Up")
            
    
    
    # ================ ANIMATION LOOP =========================
    # PRO-MOVES - can you get this while loop into a class? 
    # You will have to for PC09.
    while running:
        player.move()
        
        for target in targets:
            target.move()
       
       
        # manipulate objects here    
        if isCollision(player,target):
            target.jump()
        panel.update() # update the window with everything drawn in a single frame
        
        
    # ================ CLEANUP =========================
    if __name__ == "__main__":
        Player()
    turtle.mainloop()  # allows for user interactions; handles cleanup
run()    
    # aziz it will be cooool to add some sounds and to make the turtle disappear and appear in another posation