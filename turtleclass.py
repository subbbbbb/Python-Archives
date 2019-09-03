from turtle import *
import turtle
import random

myScreen = turtle.Screen()  # creates a new screen
myScreen.screensize(500, 500) # sets the screen size
myScreen.bgcolor("white")  # background color
myScreen.title("Oh yeah yeah")  # title of the new window

fred = turtle.Turtle()  # creates a new turtle object
fred.pencolor("cyan")
fred.color("cyan")
fred.speed("fastest")

fred.circle(50, 500, 300)


turtle.done()
