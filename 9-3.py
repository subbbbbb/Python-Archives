"""
import turtle
sam = turtle.Turtle()
sam.penup()
sam.setposition(-400,400)
sam.pendown()
for i in range(4):
    sam.forwbard(50)
    sam.right(90)
turtle.done()
"""

import turtle
sam = turtle.Turtle()
myscreen = turtle.Screen()


def regularpolygon(sides):
    angle = 360 / sides
    for i in range(sides):
        sam.forward(50)
        sam.right(angle)
        print("The triangle was printed")
        print("This will be printed every time this is run")


regularpolygon(3)
regularpolygon(5)

# Most important part of turtle is myScreen = turtle.Screen()
# and sub = turtle.Turtle()
