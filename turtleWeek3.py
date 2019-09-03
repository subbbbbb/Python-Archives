"""
import turtle
sam = turtle.Turtle()
sam.penup()
sam.setposition(-400,400)
sam.pendown()
for i in range(4):
    sam.forward(50)
    sam.right(90)
turtle.done()
"""
import turtle
sam = turtle.Turtle()
myscreen = turtle.Screen()

def regularpolygon(sides):
    angle = 360/sides
    for i in range(sides):
        sam.forward(50)
        sam.right(angle)
regularpolygon(3)
regularpolygon(5)
