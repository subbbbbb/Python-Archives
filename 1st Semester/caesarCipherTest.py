"""
def getMode():
    while True:
        mode = input("Do you want to encrypt or decrypt?")
        if(mode[0] == "e" ):
            return "Encrypt"
        elif(mode[0] == "d"):
            return "Decrypt"
        again = input("Do you want to encrypt or decrypt?")
        if(again[0] == "d"):
            return "Decrypt"
        elif(again[0] == "e"):
            return "Encrypt"
print(getMode())
"""

"""
def getMessage():
    message = input("What is the message that you want to encrypt/decrypt?")
    return message
print(getMessage())
"""

"""
def getKey():
    while True:
        key = int(input("What is the key you want to use to encrypt/decrypt?"))
        return key
print(getKey())
"""


def getTranslatedMessage(mode, message, key):
    if(mode[0] == "d"):
        key = -key
    translated = ""
    for letter in message:
        current = ord(letter)
        current += key
        translated += chr(current)
    return translated


# test case
print(getTranslatedMessage("encrypt", "hello", 1))
print(getTranslatedMessage("decrypt", "world", 2))
