import random

x = random.randint(0, 100)  # gives x a value of being a random number

minimum = 1
maximum = 100
# print(x)
guess = -1
while guess != x:
    guess = int(input("Guess a number between " +
                      str(minimum) + " and " + str(maximum)))
    if int(guess) > 100 or int(guess) < 0:
        print("Pick a number within the specified range")
    elif int(guess) > x:
        print("Your guess is higher than the number")
        maximum = guess - 1
    elif int(guess) < x:
        print("Your guess is lower than the number")
        minimum = guess - 1
    elif int(guess) == x:
        print("You got it right")
        break  # breaks out of the for loop
