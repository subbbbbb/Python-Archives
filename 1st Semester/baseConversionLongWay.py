print("Welcome to the normal to binary number converter\nEnter your number::")
normalNumber = int(input())
binaryNumber = ""
while int(normalNumber) > 0:
    if normalNumber % 2 != 0:
        normalNumber -= normalNumber/2
        binaryNumber += "1"
    elif normalNumber % 2 == 0:
        normalNumber -= normalNumber/2
        binaryNumber += "0"
string = "" 
for i in binaryNumber:
    string = i + string
    

print(string)
