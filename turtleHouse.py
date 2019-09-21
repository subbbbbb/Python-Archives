import turtle
from turtle import *

# Sets the basic turtle window
myScreen = turtle.Screen()
myScreen.title("House")
colormode(255)
myScreen.bgcolor("cyan")

# Sets the pen
sub = turtle.Turtle()
sub.pencolor("black")
sub.color("black")
sub.pensize(4)
sub.speed("fastest")

# Creates the house
sub.penup()
sub.goto(-100, 0)
sub.pendown()
sub.goto(100, 0)
sub.goto(100, 200)
sub.goto(-100, 200)
sub.goto(-100, 0)
sub.penup()

# Creates the roof for the house
sub.goto(-100, 200)
sub.pendown()
sub.goto(0, 300)
sub.goto(100, 200)
sub.penup()

# Creates the door for the house
sub.goto(-25, 0)
sub.pendown()
sub.goto(-25, 100)
sub.goto(25, 100)
sub.goto(25, 0)
sub.penup()

# Creates the window for the house
sub.goto(-75, 100)
sub.pendown()
sub.goto(-75, 150)
sub.goto(-50, 150)
sub.goto(-50, 100)
sub.goto(-75, 100)
sub.penup()

# Make the grass
sub.begin_fill()
sub.fillcolor("green")
sub.pencolor("green")
sub.color("green")
sub.goto(-400, 0)
sub.pendown()
sub.goto(400, 0)
sub.goto(400, -350)
sub.goto(-400, -350)
sub.goto(-400, 0)
sub.penup()
sub.end_fill()

# Creates the sun
sub.pencolor("yellow")
sub.color("yellow")
sub.goto(200, 200)
sub.pendown()
sub.begin_fill()
sub.fillcolor("yellow")
sub.circle(30)
sub.end_fill()
