"""
# Question 1:
# a.
x = int(input())
# b.
y = float(input())
# c.
z = input()
# d.
print(float(x) * y)
# e.
print(x%2)
# f.
print("You entered the following string: " + z)
"""

"""
# Question 2 (sumDigits):
number = int(input())
finalNumber = 0
while number > 0:
    finalNumber += number % 10
    number = number // 10
print(finalNumber)
"""

"""
# Question 3 (coinProblem)
dollarAmount = float(input("Enter your dollar amount in a decimal number::"))
dollarCoins = 0
halfDollars = 0
pennies = 0
while dollarAmount > -1:
    dollarCoins += dollarAmount//1
    dollarAmount -= (dollarCoins * 1)
    print("Dollar Coins: " + str(dollarCoins))

    halfDollars += dollarAmount//0.5
    dollarAmount -= (halfDollars * 0.5)
    print("Half Dollar Coins: " + str(halfDollars))

    pennies += dollarAmount//0.01
    dollarAmount -= (pennies * 0.01)
    print("Pennies: " + str(pennies))
    break
"""

