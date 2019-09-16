# sub and mikias

# guess = int(input("Guess a number between " + str(minimum) + " and " + str(maximum)))
myGrade = int(input("What did you get on your test? (in percent)"))
# print("What did you get on your test? (in percent)")
# myGrade = input()
if int(myGrade) < 60:
    print("You got an F ")
elif int(myGrade) > 59 and int(myGrade) < 70:
    print("Barely passed with a D")
elif int(myGrade) > 69 and int(myGrade) < 80:
    print("you got a C")
elif int(myGrade) > 79 and int(myGrade) < 90:
    print("damn you got an A")
elif int(myGrade) > 100:
    print("liar")
