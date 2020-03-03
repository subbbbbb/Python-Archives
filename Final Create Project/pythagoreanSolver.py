import math

def main():
    choice = input("Do you want to solve for angle measures or lengths?")
    if(choice == "angle measures"):
        angles = getAngles()
    elif(choice == "lengths"):
        lenghts = getLengths()
    

def getLengths():
    typeOfTriangle = input("Do you want to solve for the hypotenuse or a leg of the triangle?")
    if(typeOfTriangle == "hypotenuse"):
        sideA = int(input("Enter in the length for the first side"))
        sideB = int(input("Enter in the length for the second side"))
        sideC = math.sqrt(math.pow(sideA,2) + math.pow(sideB,2))
        print("Your hypotenuse is " + str(sideC) + " units.")
    if(typeOfTriangle == "leg"):
        hypotenuse = int(input("Enter in the length of the hypotenuse"))
        leg2 = int(input("Enter in the length of the leg that you know of"))
        leg1 = math.sqrt(math.pow(hypotenuse,2)-math.pow(leg2,2))
        print("The length of your leg is " + str(leg1) + " units.")

# def getAngles():

main()


