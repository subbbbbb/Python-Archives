def getMode():
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