import matplotlib.pyplot as plt
import math
import numpy as np

global coefficients

coefficients = []

def main():
    global coefficients
    global dis
    coefficients = getCoefficients()
    xints = xintercepts()
    vtx = getVertex()
    x = np.linspace (-10, 10, 1000)
    y = coefficients[0] * x**2 + coefficients[1] * x + coefficients[2]
    fig, ax = plt.subplots()
    ax.grid(True, which='both')
    # set the x-spine
    ax.spines['left'].set_position('zero')

    # turn off the right spine/ticks
    ax.spines['right'].set_color('none')
    ax.yaxis.tick_left()

    # set the y-spine
    ax.spines['bottom'].set_position('zero')

    # turn off the top spine/ticks
    ax.spines['top'].set_color('none')
    ax.xaxis.tick_bottom()    
    if dis > 0:
        ax.plot(0,coefficients[2],'ro')
        ax.plot(xints[0],0,'go')
        ax.plot(xints[1],0,'go')
        ax.plot(vtx[0], vtx[1], 'bo')
        ax.plot(x,y)
    elif dis == 0:
        ax.plot(0,coefficients[2],'ro')
        ax.plot(xints,0,'go')
        ax.plot(vtx[0], vtx[1],'bo')
        ax.plot(x,y)
    else:
        pass
    plt.show()
    print("The y-intercept is" + "(0," + str(coefficients[2]) + ")")
def getCoefficients():
    global coefficients
    for i in range(3):
        coefficients.append(int(input("Enter an integer for the x^" + str(2-i) + "coefficient: ")))
    return coefficients

def xintercepts():
    global coefficients
    global dis
    dis = coefficients[1]**2 - 4*coefficients[0]*coefficients[2]
    if dis  > 0:
        x1 = (-1*coefficients[1] + dis**(1/2))/(2*coefficients[0])
        x2 = (-1*coefficients[1] - dis**(1/2))/(2*coefficients[0])
        print(str(x1) + " and " + str(x2))
        return (x1, x2)
    elif dis == 0:
        xint = (-1*coefficients[1] + dis**(1/2))/(2*coefficients[0])
        print(xint)
        return xint
    else:
        print("Non-real x-intercepts, cannot be graphed")
        
def getVertex():
    global coefficients
    xvertex = (-1*coefficients[1])/(2*coefficients[0])
    yvertex = coefficients[0] * xvertex**2 + coefficients[1] * xvertex + coefficients[2]
    print("The vertex of the graph is (" + str(xvertex) + "," + str(yvertex) + ")")
    return (xvertex,yvertex)    
    
main()


