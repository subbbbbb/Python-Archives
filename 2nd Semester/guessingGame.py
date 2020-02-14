import random 

global minimum, maximum
maximum = 100
minimum = 1

def pickNumber(): # the method that picks a number for you
    global minimum, maximum
    number = random.randint(1, 100)
    return number

def userGuess(counter): # the method that asks the user for a guess
    global minimum, maximum
    print("Guess between ", minimum , " and " ,maximum)
    guess = int(input('Enter your guess: '+ str(counter)))
    return guess

def giveFeedback(guess, number, c): # the method that tells you whether your guess was too high or too low
    global minimum, maximum
    if guess > number:
        print('Too High')
        maximum = guess - 1
    elif guess < number:
        print('Too Low')
        minimum = guess + 1
    else:
        print('Just Right')
        print(c, "guesses")
    

def run(): # the looping method that keeps the program running
    number = pickNumber()
    guess = -1
    count = 0
    while guess != number:
        count+=1
        guess = userGuess(count)
        giveFeedback(guess, number, count)
  
run()