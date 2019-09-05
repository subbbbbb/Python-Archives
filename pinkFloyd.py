# My attempt at drawing the Pink Floyd Dark Side of the Moon album cover in Python Turtle

# All the import statements needed
import turtle
from turtle import *
import random
from random import randint

# Declares the turtle screen and gives the window a name
myScreen = turtle.Screen()
myScreen.title("Dark Side of the Moon")
myScreen.bgcolor("black")

# Creates a new pen object
sub = turtle.Turtle()
sub.pencolor("white")
sub.color("white")
sub.pensize(5)
sub.speed("slow")

# Puts the pen down and starts writing the triangle
sub.goto(-100,0)
sub.pendown()
sub.forward(200)          
sub.right(-120)       
    
sub.forward(200)          
sub.right(-120)           
sub.forward(200)          
sub.right(-120)

# Adds the Pink Floyd text
sub.penup()
sub.goto(0,200)
colormode(255)
red1 = randint(0,255)
blue1 = randint(0,255)
green1 = randint(0,255)
sub.pencolor(red1,blue1,green1) # randomizes the color of the text
sub.write("Pink Floyd: Dark Side of the Moon", True, align= "center", font=("Arial", 24, "bold"))
sub.pencolor("white")
sub.pendown()
x = 1
sub.goto(25,50) # Does the little line to the triangle

# Does the RGB line that is supposed to replicate a rainbow
while x < 600: # This makes it so that 600 isoceles triangles will be printed
    cool = turtle.Turtle()
    x+=1 # Every time it iterates through the while loop the triangles get bigger
    colormode(255) # Allows you to use the 255 RGB colors ***I think***
    cool.pensize(1)
    cool.speed(100)
    red = randint(0,255)
    green = randint(0,255) # I would've used the randints above but that way the colors won't change
    blue = randint(0,255)
    cool.pencolor(red,green,blue) # this will make it some random color
    cool.forward(40 + x) # it is 50 + x because the rainbow gets bigger as x+=1
    cool.right(200)
    
sub.done()