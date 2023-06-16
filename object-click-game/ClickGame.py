#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 18:22:18 2021

Created on WHAT DAY IS IT?

@author: Robert Lino

WHAT DOES YOUR GAME DO? The game test how fast one can move from side to side within 10 seconds
    OBJECTIVE - Use your fingers to speed up the object and also turn to change direction
    RULES - The left key on the keyboard turns left and the right turns right and the up key speeds up the object
    CHALLENGE - How fast can one change directions after hitting the limits
    INTERACTIONS - Hand and response time
"""
import time
import turtle

panel = turtle.Screen()
panel.title("Move Across the Screen as fast you can!")
panel.bgpic("bedrock-sign.gif")
panel.bgcolor("magenta")
w = 800
h = 800
panel.setup(width=w, height=h)

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.speed = 3
        self.penup()
        self.shape("turtle")
        self.color("red")
        self.shapesize(3)
        
    def move(self):
        '''This checks the boundaries'''
        
        self.forward(self.speed)
        if self.xcor()>290 or self.xcor() < -290:
            self.left(60)
        if self.ycor()>290 or self.ycor() <-290:
            self.left(60)
          
    def turnleft(self):
        '''It makes the object turn left using the left key of the keyboard'''
        self.left(45)
    def turnRight(self):
        '''It makes the object turn right using the right key of the keyboard'''
        self.right(45)
    def speedUp(self):
        '''It increases the speed of the object when the up key on the keyboard is press'''
        self.speed += 1
        
        
player = Player()

#class instances
turtle.listen()
turtle.onkey(player.turnleft, "Left")
turtle.onkey(player.turnRight, "Right")
turtle.onkey(player.speedUp,"Up")
time_limit = 10
start_time = time.time()
while True:
    elapsed_time = time.time() -start_time
    print(time_limit - int(elapsed_time))
    if elapsed_time > time_limit:
        print("GAME OVER")
        quit()
       
   
        
    player.move()
    panel.update()
    
   