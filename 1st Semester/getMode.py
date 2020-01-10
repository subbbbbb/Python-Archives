# getMode method
def getMode():
    mode = input("Do you want to encrypt or decrypt your message?").lower()
    while True:  # the while loop is there so the program will continue to run
        if(mode == "encrypt" or mode == "decrypt"):
            return mode
        else:
            print("Enter in encrypt or decrypt:")
            mode = input(
                "Do you want to encrypt or decrypt your message?").lower()


print(getMode())
