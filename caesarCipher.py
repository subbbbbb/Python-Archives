
# getMode() is a getter method that either prints out decrypt/encrypt, or tells you to do it over again if invalid input


def getMode():  # defines the specific mode that you want
    # converts single letters to lowercase to preventp roblems later
    mode = input("do you want to encrypt or decrypt?").lower()
    # loop that is always true (as long as the user enters an input)
    while True:
        if(mode == "encrypt" or mode == "decrypt"):  # if the user types in an input correctly
            return mode  # don't print, but return what they type
        else:
            # if not, make them try again by using the mode line from earlier
            print("Spell it correctly and try again")
            mode = input("Spell it right and try again::").lower()


print(getMode())  # outside of the function, make sure to test it to see if it works


# getMessage() is a getter method that returns what method you want (same as getMode)
def getMessage():
    # remember to use return statements inside of the functions instead of print statements
    return input("Encrypt or Decrypt")


print(getMessage())  # use the print statement outside of the function to check


# another getter method that simply gives you the key that you enter, as long as it is between 1 and 25
def getKey():
    # asking for a key and convert to int
    key = int(input("Enter a number betwen -25 and 25"))
    while True:  # while the user provides some kind of input --
        if key >= -25 and key <= 25:
            return key
    else:
        key = int(input("I need a number 1-25"))


print(getKey())



def getTranslatedMessage(mode, message, key):  # parameter list
    if mode[0] == 'd':  # if first letter in mode variable is d grab part of string
        key = -key  # switch key for decryption
    translated = ""
    for letter in message:
        num = ord(letter)
        num = num + key
        translated += chr(num)
    return translated

print(getTranslatedMessage("encrypt", "Hello", 1))
print(getTranslatedMessage("decrypt", "Ifmmp", 1))
print(getTranslatedMessage("encrypt", "Sub", 2))

# getMode() is a getter method that either prints out decrypt/encrypt, or tells you to do it over again if invalid input
# defines the specific mode that you want
# converts single letters to lowercase to prevent problems later
# loop that is always true (as long as the user enters an input)
# if the user types in an input correctly
# don't print, but return what they type
# if not, make them try again by using the mode line from earlier
# outside of the function, make sure to test it to see if it works
# getMessage() is a getter method that returns what method you want (same as getMode)
# remember to use return statements inside of the functions instead of print statements
# use the print statement outside of the function to check
# another getter method that simply gives you the key that you enter, as long as it is between 1 and 25
# asking for a key and convert to int
# while the user provides some kind of input --
# parameter list
# if first letter in mode variable is d grab part of string
# switch key for decryption
