import math


def main():
    choice = input(
        "Do you want to solve for angle measures, lengths, or law of sines?")
    if("angle" in choice):
        getAngles()
    elif("length" in choice):
        getLengths()
    elif("law" in choice):
        lawOfSin()


def getLengths():
    print("Keep in mind, this code only works for right triangles")
    typeOfTriangle = input(
        "Do you want to solve for the hypotenuse or a leg of the triangle?")
    if(typeOfTriangle == "hypotenuse"):
        sideA = float(input("Enter in the length for the first side"))
        sideB = float(input("Enter in the length for the second side"))
        sideC = math.sqrt(math.pow(sideA, 2) + math.pow(sideB, 2))
        print("Your hypotenuse is " + str(sideC) + " units.")
    if(typeOfTriangle == "leg"):
        hypotenuse = float(input("Enter in the length of the hypotenuse"))
        leg2 = float(input("Enter in the length of the leg that you know of"))
        leg1 = math.sqrt(math.pow(hypotenuse, 2) - math.pow(leg2, 2))
        print("The length of your leg is " + str(leg1) + " units.")


def getAngles():
    numOfAngles = int(input("How many angle measures do you know already?"))
    if(numOfAngles == 1):
        validity = input(
            "Do you know at least: a) two angles and one side, b) two sides and a non-included angle, c) three sides, d) two sides and the included angle")
        if(validity == "yes"):
            lawOfSin()
    if(numOfAngles == 2):
        angleA = float(input("Enter in the angle measure for the first side"))
        angleB = float(input("Enter in the angle measure for the second side"))
        angleC = 180 - (angleA + angleB)
        print("The angle measure of the unknown angle is " +
              str(angleC) + " degrees.")


def lawOfSin():
    angleA = float(input("enter angle A"))
    sideA = float(input("enter side A"))
    extra = float(input("enter the extra side or angle"))
    angleA= math.radians(angleA)
    option = input("For this equation to work you must have a) two sides and an included angle b) two angles and an included side")
    if(option == "a"):
        print(math.degrees(math.asin(math.sin(angleA)/sideA*extra)))
    elif(option == "b"):
        print(math.sin(math.radians(extra))*sideA)/math.sin(angleA)
main()
