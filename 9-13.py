import turtle
screen = turtle.Screen()
screen.setup(500,500)
screen.tracer(0)
don = turtle.Turtle()
don.speed(0)
don.width(3)
don.hideturtle()
def draw_square():
    for side in range(4):
        don.forward(100)
        don.left(90)
don.penup()
don.goto(-350,0)
don.pendown()
while True:
    don.clear()
    draw_square()
    screen.update()
    don.forward(0.02)
