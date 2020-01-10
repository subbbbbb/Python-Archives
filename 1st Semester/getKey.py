def getKey():
    key = int(input("What is the key that you want to use to encrypt/decrypt?"))
    while True:  # autoloop in case wrong input
        if(key <= 25 and key >= -25):
            return key
        else:
            print("Your key is not in the range of -25 to 25.")
            key = int(
                input("What is the key that you want to use to encrypt/decrypt?"))


print(getKey())
