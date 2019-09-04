import turtle
from turtle import *
import random

myScreen = turtle.Screen()
myScreen.screensize(500,500)
myScreen.bgpic("steveharvey.jpeg")
myScreen.title("Python Turtle House")

sub = turtle.Turtle()
sub.pencolor("green")
sub.speed("fast")

sub.goto(100,100)
sub.circle(100,100,50)

turtle.done()