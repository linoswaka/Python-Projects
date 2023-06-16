#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Robert Lino
May 29, 2020
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======
#This segment of the code draws a circle with a radius of 85 at the finger tips of Jeff

turtle.shape("turtle") # sets turtle shape
turtle.hideturtle()    #Hides turtle
turtle.pen(pencolor="yellow",fillcolor="red",pensize=5) # sets the pen color, fill color and pen size
turtle.up()            #Pulls turtle up
turtle.goto(111,-90) # Sets the circle at finger tips
turtle.down()          #pulls turtle down
turtle.begin_fill()    #Begins filling
turtle.circle(85) #Draws a circle with a radius of 85
turtle.end_fill()      #Ends fill
#turtle.reset()           #This function deletes the shape and resets it to default

#This segment of the program draws a 100x60 rectangle at the nose of Jeff

turtle.pencolor(41,41,253) #Sets the color to blue(RGB)
turtle.pensize(8)          #Sets the width of the pen
turtle.up()
turtle.goto(24,84)         #Starts the shape at nose
turtle.down()
turtle.forward(100)        #Moves the pen forward 100 pixels
turtle.left(90)            #Turns the pen left 90 degrees
turtle.forward(60)         #Turns the pen 60 pixels forward
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(60)
turtle.left(90)
# turtle.reset()            #This function deletes the shape and resets it to default

#This segment draws a 100x100 pixel square at the left eye of Jeff

turtle.pen(pencolor="pink",pensize=8)   # Sets the pen color pink
turtle.up()
turtle.goto(-15,108)                    #It starts drawing the square at the left eye
turtle.down()
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.reset()           #This function deletes the shape and resets it to default

# #this segment of the code draws a five sides shape at the right shoulder of Jeff

turtle.pen(pencolor="yellow",pensize=5)    #Sets up the pen color to yellow and the size to 5
turtle.up()
turtle.goto(146,-63)                       #Starts the shape at the right shoulder
turtle.down()
turtle.circle(100, steps=5)                #This code draws a five figure shape
turtle.left(20)                            #Moves the pen 20 pixels to the left
turtle.reset()           #This function deletes the shape and resets it to default

#The segment of the code draws a 9 figure shape at the left forehead of Jeff

turtle.pen(pencolor="green",pensize=5)     #Sets color and size of the pen
turtle.up()
turtle.goto(-25,-185)                      #Starts the shape at the left forehead
turtle.down()
turtle.circle(100, steps=9)                #Draws a 9 corner shape 
turtle.left(20)
turtle.reset()          #This function deletes the shape and resets it to default

#The segment of the code draws a 9 figure shape
turtle.pen(pencolor="red",pensize=5)     #Sets color and size of the pen
turtle.up()
turtle.goto(25,10)                      #Starts the shape at the chin
turtle.down()
turtle.circle(100, steps=3)                #Draws a 3 corner shape 
turtle.left(20)
turtle.reset()          #This function deletes the shape and resets it to default


#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
turtle.done()

