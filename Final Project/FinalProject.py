#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 11:27:44 2021
This code creates a greeting card with dooms,pillars,lamps,crescent and greetings

@author: Robert Lino and Abdelaziz Almaiyouf
"""

import turtle,random

# ==== Libray settings==========
turtle.title("Greeting Card")
turtle.colormode(255)
turtle.hideturtle()
panel = turtle.Screen()
panel.bgcolor(0,0,0)

w = 700
h = 450
panel.setup(width=w, height=w)

#=========CLASSES===========

#This class draws the dooms, cresecents, pillars and lamps on the greeting card
class cardDrawings(turtle.Turtle):
    def __init__(self, radius, location, angle):
        super().__init__()
        self.radius = radius
        self.location = location
        self.angle = angle
        self.hideturtle()
        self.speed(10)
        self.pensize(5)
        self.color('gold')
  
    def drawLine(self):  
        ''' This function draws the baselines for the dooms'''
        self.up()
        self.goto(-350,0)
        self.down()
        self.forward(50)
        self.up()
        self.goto(300,0)
        self.down()
        self.forward(50)
        self.color('gold')

    def drawDoom(self):
        '''This function draws dooms and it takes locations and radius'''
        self.up()
        self.color('gold')
        self.goto(self.location)
        self.down()
        self.left(90)
        self.circle(self.radius,self.angle)
        self.left(90)
        
    def drawPillars(self):
        ''' This functions draw pillars and takes locations with fixed lenght'''
        self.up()
        self.left(90)
        self.goto(self.location)
        self.down()
        self.forward(40)
    
    def drawCrescent(self):
        '''This function draws a crescent on top of pillars using two circles with different colors'''
        self.left(90)
        self.up()
        self.goto(self.location)
        self.down()
        self.circle(10,360) # first circle that makes the base of the crescent(black)
        self.color("black") 
        self.pensize(8)
        self.begin_fill()
        self.circle(7,360) # Second circle that shapes the crescent(white)
        self.end_fill()
       
    def drawLamp(self):
        '''this function draws the lamp and fills it with the yellow color'''
        self.up()
        self.goto(self.location)
        self.down()
        self.color ('black','yellow')
        self.begin_fill()
        self.circle(self.radius,self.angle)
        self.end_fill()
        
#This class draws the sky objects; moon and stars
class cardSky(turtle.Turtle):
    def init(self,location):
        self.speed(10)
        
    def drawStar(self):
        ''' This function draws stars in random location'''
        self.hideturtle()
        self.color("silver","silver")
        x = random.randint(-350,350)
        y = random.randint(150,225)
        self.pensize(2)
        self.up()
        self.goto(x,y)
        self.begin_fill()
        self.down()
        #This loop determines the number of star corners
        for i in range(5): #
            self.forward(10)
            self.right(144)
        self.end_fill()
        
    def drawMoon(self):
        '''This function draws a crescent on top of pillars using two circles with different colors'''
        self.hideturtle()
        self.up()
        self.left(90)
        self.goto(200,200)
        self.down()
        self.begin_fill()
        self.circle(50,360) # first circle that makes the base of the crescent(black)
        self.color("white","white") 
        self.end_fill()
        self.penup()
        self.left(-10)
        self.pensize(8)
        self.goto(180,200)
        self.pendown()
        self.begin_fill()
        self.color("black","black") 
        self.circle(44,360) # Second circle that shapes the crescent(white)
        self.end_fill()


# This class draws and write the greetings
class cardGreeting(turtle.Turtle):
    def init(self,location,size,color,font):
        self.speed(17)
        self.location = location
        self.size = size
        self.color= color
        self.font = font
        
    def drawE(self):
        '''This function draws the letter E'''
        self.hideturtle()
        self.penup()
        self.pencolor('green') # 
        self.pensize(10)
        self.goto(-30,-175)
        self.pendown()
        self.backward(50)
        self.left(90)
        self.forward(100)
        self.right(90)
        self.forward(50)
        self.penup()
        self.goto(-30,-125)
        self.pendown()
        self.backward(50)

    def drawI(self):
        '''This function draws the letter I'''
        self.hideturtle()
        self.penup()
        self.pencolor('red') # 
        self.pensize(10)
        self.goto(0,-175)
        self.pendown()
        self.right(90)
        self.backward(50)
        self.penup()
        self.goto(0,-100)
        self.pendown()
        self.backward(5)
         
    def drawD(self):
        '''This function draws the letter D'''
        self.hideturtle()
        self.penup()
        self.pencolor('orange') # 
        self.pensize(10)
        self.goto(30,-175)
        self.pendown()
        self.right(180)
        self.forward(100)
        self.right(90)
        self.circle(-50,180)
        self.penup()

    def writeGreeting(self):
        '''This function writes the word mubarak'''
        self.goto(-160,-300)
        self.pendown()
        self.color("white")
        self.write("Mubarak", font=("Arial",80,"italic bold"))

    

# ============Object initiations===============

doomLines = cardDrawings(0,0,0)
doomRadius = [-20, -30, -40, -120, -40, -30, -20] # radius for the dooms
doomLocation = [(-300,0),(-260, 0), (-200, 0), (-120, 0),(120, 0), (200, 0), (260, 0)]#location for the dooms
pillarsLocation = [(-280,20),(-230,30),(-160,40),(0,120),(160,40),(230,30),(280,20)]  #location for the pillars on which the crescent sits
crescentLocation = [(-270,70),(-220,80),(-150,90),(10,170),(170,90),(240,80),(290,70)]  # location for the cresecnt
lampLocationup = [(-170, -70),(230, -70)] # location for the upper shape of the lamp
lampLocationdn = [(-170,-150),(230,-150)] # location for the lower shape of the lamp
lamppillarsLocation = [(-200,-40),(200,-40)] # location for the pillars of the lapm
lampshapeLocation = [(-200,-160),(200,-160)] #location for the middle shape of the lamp
star = cardSky()
moon = cardSky()


moon.drawMoon() # Draws the moon

for i in range(10):
    star.drawStar()



doomLines.drawLine()
for i in range(7):
        dooms = cardDrawings(doomRadius[i],doomLocation[i],180)
        dooms.drawDoom()
        pillars = cardDrawings(0,pillarsLocation[i],0 )
        pillars.drawPillars()
        crescents = cardDrawings(0,crescentLocation[i],0 )
        crescents.drawCrescent()
        
# This for loop is for the dooms and lamps
for i in range(2):
        lampsdoomup = cardDrawings(30,lampLocationup[i],180 )
        lampsdoomup.drawDoom()
        lampsdoomdn = cardDrawings(30,lampLocationdn[i],-180 )
        lampsdoomdn.drawDoom()
        lamppillars = cardDrawings(0,lamppillarsLocation[i],0 )        
        lamppillars.drawPillars()
        lampshape = cardDrawings(50,lampshapeLocation[i],360)        
        lampshape.drawLamp()



letter = cardGreeting()
letter.drawE() 
letter.drawI() 
letter.drawD()     
letter.writeGreeting()  

       
turtle.done()
