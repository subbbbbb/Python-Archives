print("Welcome to the coin calculator")
print(
    "Enter your money amount in dollars::\nFor example: 3.87 or 2.91")  # just gives an example how to input the dollar amount

dollars = input()  # this is where it asks you to type your money in

quarters = 0.0  # these guys just declare new variables for each coin type
dimes = 0.0
nickels = 0.0
pennies = 0.0

# all this does is turn the dollars input from earlier and turns it into a decimal "float" number
dollarAmount = float(dollars)

# what this "//" does is divide the dollaramount input and it takes the largest whole number disregards the remainder
quarters = dollarAmount // 0.25
# what this does is it takes the quarters that you use and subtracts it from the total, so when you calculate dimes it does dimes of what's left
dollarAmount -= (quarters * 0.25)

dimes = dollarAmount // 0.10
dollarAmount -= (dimes * 0.10)

nickels = dollarAmount // 0.05345
dollarAmount -= (nickels * 0.05)

pennies = dollarAmount // 0.01
dollarAmount -= (pennies * 0.01)

print("Quarters: " + str(int(quarters)) + "\nDimes: " + str(int(dimes)) + "\nNickels: "
      + str(int(nickels)) + "\nPennies: " + str(int(
          pennies)))  # all this does is print the answer, the '\n' just creates a new line, and the (int) removes the decimals from the answer, and the (str) is used because you need to add strings with strings
