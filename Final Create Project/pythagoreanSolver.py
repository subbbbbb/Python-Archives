import math

global choice

def main():
    choice = input("Do you want to solve for angle measures, lengths, or law of sines/cosines?")
    if(choice == "angle measures"):
        angles = getAngles()
    elif(choice == "lengths"):
        lengths = getLengths()

def getLengths():
    print("Keep in mind, this code only works for right triangles")
    typeOfTriangle = input("Do you want to solve for the hypotenuse or a leg of the triangle?")
    if(typeOfTriangle == "hypotenuse"):
        sideA = float(input("Enter in the length for the first side"))
        sideB = float(input("Enter in the length for the second side"))
        sideC = math.sqrt(math.pow(sideA,2) + math.pow(sideB,2))
        print("Your hypotenuse is " + str(sideC) + " units.")
    if(typeOfTriangle == "leg"):
        hypotenuse = float(input("Enter in the length of the hypotenuse"))
        leg2 = float(input("Enter in the length of the leg that you know of"))
        leg1 = math.sqrt(math.pow(hypotenuse,2)-math.pow(leg2,2))
        print("The length of your leg is " + str(leg1) + " units.")

def getAngles():
    numOfAngles = int(input("How many angle measures do you know already?"))
    if(numOfAngles == 1):
        validity = input("Do you know at least: a) two angles and one side, b) two sides and a non-included angle, c) three sides, d) two sides and the included angle")
        if(validity == "yes"):
            lawOfSinCos()
    if(numOfAngles == 2):
        angleA = float(input("Enter in the angle measure for the first side"))
        angleB = float(input("Enter in the angle measure for the second side"))
        angleC = 180 - (angleA + angleB)
        print("The angle measure of the unknown angle is " + str(angleC) + " degrees.")

def lawOfSinCos():
    print("Enter in a, b, c, or d depending on what you want to solve for:")
    whichCase = input("a) two angles and one side, b) two sides and a non-included angle, c) three sides, d) two sides and the included angle")    
    if(whichCase == "a"): # doesn't work properly yet
        angleB = float(input("What is the measure of the angle opposite to the side you want to find:"))
        angleA = float(input("What is the measure of the other angle:"))
        angleC = 180 - angleA - angleB
        sideA = float(input("What is the length of the included side? (corresponding to A or B)"))
        missingSide = (sideA*math.sin(angleB))/(math.sin(angleC))
        print("The length of the missing side is " + str(missingSide) + " units.")
lawOfSinCos()
