
print("This will add the digits that you enter.")
number = int(input("Enter a number::"))
totalNumber = 0
while number > 0:
    totalNumber += number % 10
    number = number // 10


print(totalNumber)

# parts on the test next week - sumDigits,
# guessingGame, dollarsToCoins, base10Tobase2
