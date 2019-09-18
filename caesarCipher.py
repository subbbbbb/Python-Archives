<<<<<<< HEAD
 
# getMode() is a getter method that either prints out decrypt/encrypt, or tells you to do it over again if invalid input
def getMode(): #defining mode
    mode =  input("do you want to encrypt or decrypt?").lower()#convert single letters to lowercase
    while True: #loop
=======

def getMode(): # basically a getter method for getting the type you want (encrypt or decrypt)
    
    mode =  input("Would you like to encrypt or decrypt?").lower() #convert single letters to lowercase, prevents problems with ASCII
    while True: # always true, as long as the input is
>>>>>>> a6eb884b377e35498aa3940612abebfb4fc7fc21
        if mode == "encrypt" or mode == "decrypt": #saying what the user will do 

            return mode #returning mode
        else:
            mode = input("Spell it right and stop wasting my time").lower() #spell it right       
print(getMode()) # print it
 

 
# getMessage() is a getter method that returns what method you want (same as getMode)
def getMessage(): 
    return input("Encrypt or Decrypt")
print(getMessage())
 

# Ask Mr. Sarnowski about this method, since at this point it does not seem to work
def getKey():
    try:
        key = int(input("enter key between 1-25"))
        return key
    except:
        key = int(input("Enter key between 1-25"))
 

# another getter method that simply gives you the key that you enter, as long as it is between 1 and 25
def getKey ():
    key = int(input("Enter a number betwen -25 and 25")) # asking for a key and convert to int
    while True:
        if key >=-25 and key<=25:
            return key
    else:
        key = int(input("I need a number 1-25"))
print(getKey())

<<<<<<< HEAD

=======
>>>>>>> a6eb884b377e35498aa3940612abebfb4fc7fc21

def getTranslatedMessage(mode, message, key): #parameter list
    if mode[0] == 'd': #if first letter in mode variable is d grab part of string
        key = -key #switch key for decryption
    translated = ""
    for letter in message:
        num = ord(letter)
        num = num +key
        translated += chr(num)
    return translated 
print(getTranslatedMessage("encrypt", "Hello", 1))
print(getTranslatedMessage("decrypt", "Ifmmp", 1))
print(getTranslatedMessage("encrypt", "Sub", 2))
