import random

x = random.randint(0,100)

minimum = 0
maximum = 100

guess = int(input("Enter in a number from 0 to 100::"))
while(guess != x):
    if(guess > maximum or guess < minimum):
        print("Enter a number in the specified range.")
    if(guess > x):
        print("Your guess is too high")
        maximum = guess
    if(guess < x):
        print("Your guess is too low")
        minimum = guess
print("You got the correct answer")