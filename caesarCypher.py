"""Define a function to ask user if they want to encrypt or decrypt and return the answer"""
def getMode(): # empty paramter list
    mode = input("Do you wish to encrypt or decrypt?").lower()
    while True:
        mode = input("Do you wish to to encrypt or decrypt?").lower()
        if mode == "encrypt" or mode == "decrypt":
            return mode
        else:
           mode = input("Do you wish to to encrypt or decrypt?").lower()
# print(getMode())


def getMessage():
    return input("What is your message?")
# print(getMessage())

def getMessage():
    return input("What is your message?")
# print(getMessage())

def getKey(): # gets the key for the cipher
    key = int(input("Enter a key between 1 and 25"))
    while True:
        if key >= -25 and key <= 25:
            return key
        else:
            key = int(input("Enter a key between 1 and 25"))

def getTranslatedMessage(mode, message, key): # parameter list
    if mode[0] == "d": # if first letter in mode variable is d
        key = -key # switch key for decryption

    translated = "" # variable for storing translated message
    for letter in message: # looks at each letter in message 
        num = ord(letter)
        num += key 
        translated += chr(num)

    return translated
