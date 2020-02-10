import random 

def pickNumber(): # the method that picks a number for you
    number = random.randint(1, 100)
    return number

def userGuess(): # the method that asks the user for a guess
    guess = int(input('Enter your guess: '))
    return guess

def giveFeedback(guess, number): # the method that tells you whether your guess was too high or too low
    min = 0
    max = 100
    if guess > number:
        print('Too High')
        #max = guess
        #print("Enter a guess between " + min + " and " + max)
    elif guess < number:
        print('Too Low')
        #min = guess
        #print("Enter a guess between " + min + " and " + max)
    else:
        print('Just Right')

def run(): # the looping method that keeps the program running
    number = pickNumber()
    guess = -1
    count = 0
    while guess != number:
        count+=1
        guess = userGuess()
        giveFeedback(guess, number)
    print("You guessed the right number in " + str(count) + " guesses")
run()