import matplotlib.pyplot as plt
import math
import numpy as np

global coefficients

coefficients = []

def main():
    global coefficients
    coefficients = getCoefficients();
    xints = xintercepts()
    fig, ax = plt.subplots();
    ax.grid(True,which = "both")

    ax.spines["left"].set_position("zero")

    ax.spines["right"].set_color("none")
    ax.yaxis.tick_left()

    ax.spines["bottom"].set_position("zero")

    ax.spines["top"].set_color("none")
    ax.xaxis.tick_bottom()
    ax.plot(0,coefficients[2],"ro")
    ax.plot(xints[0],0,"go")
    ax.plot(xints[1],0,"go")
    plt.show()     


def getCoefficients():
    global coefficients
    for i in range(3):
        coefficients.append(int(input("Enter an integer for the x^" + str(2-i) + " coefficient")))

    """
    coefficients.append(int(input("Enter an integer for the x^2 coefficient")))
    coefficients.append(int(input("Enter an integer for the x^1 coefficient")))
    coefficients.append(int(input("Enter an integer for the x^0 coefficient")))
    """
    return coefficients

def xintercepts():
    global coefficients
    discriminant = coefficients[1]**2 - 4*coefficients[0]*coefficients[2]
    if discriminant > 0:
        x1 = (-coefficients[1] + discriminant**(1/2)) / (2*coefficients[0])
        x2 = (-coefficients[1] - discriminant**(1/2)) / (2*coefficients[0])
        return(x1, x2)
    elif discriminant == 0:
        print("hello")
    else:
        print("goodbye")
main()

