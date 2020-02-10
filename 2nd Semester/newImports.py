import matplotlib.pyplot as plt
import math
import numpy as np

def quadratic (a,b,c):
    x = np.linspace(-10,10,1000)
    y = a*x**2 + b*x + c
    d = b**2 - 4 * a * c

    fig, ax = plt.subplots()
    ax.grid(True, which="both")
    ax.spines["left"].set_position("zero")
    ax.spines["right"].set_position("none")
    ax.yaxis.tick_left()

    ax.spines["top"].set_color("none")
    ax.xaxis.tick_bottom()
    ax.plot(0,c,"ro")

    if(d == 0):
        convex_point = -b/(2*a)
        ax.plot(convex_point,0,"ro")
        print("The convex point is at", convex_point, "on the axis | the parabola intersect the y-axis"
    elif(d < 0):
        print("Determinant is", d, "and if determinant is smaller than zero, there is no real solution")
    else:
        x_positive = (-b + math.sqrt(d))/(2*a);
        x_negative = (-b - math.sqrt(d))/(2*a);
        ax.plot(x_poitive,0,"ro")
        ax.plot(x_negative,0,"ro")
        print("the convex points is at", convex_point, "on the x-axis | x_positive", x_positive, "|x_negative")
    ax.plot()
    plt.show()

quadratic(1, -5, 6)
