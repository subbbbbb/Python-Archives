import turtle
from turtle import *
import random
from random import randint

myScreen = turtle.Screen()
myScreen.title("House")
colormode(255)
myScreen.bgcolor("cyan")

sub = turtle.Turtle()
sub.pencolor("black")
sub.color("black")
sub.pensize(4)
sub.speed("slow")

sub.penup()
sub.goto(-100,0)
sub.pendown()
sub.goto(100,0)
sub.goto(100,200)
sub.goto(-100,200)
sub.goto(-100,0)
sub.penup()
sub.goto(-100,200)
sub.pendown()
sub.goto(0,300)
sub.goto(100,200)
sub.penup()
sub.goto(-50,0)
sub.pendown()
sub.goto(-50,50)
sub.goto(50,50)
sub.goto(50,0)

