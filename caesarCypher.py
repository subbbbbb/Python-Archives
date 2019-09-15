'''
def getMode(): #defining mode
    
    mode =  input("you wanna encrypt or decrypt dummy?").lower()#convert single letters to lowercase
    while True: #loop
        if mode == "encrypt" or mode == "decrypt": #saying what the user will do 

            return mode #returning mode
        else:
            mode = input("Spell it right and stop wasting my time").lower() #spell it right
            
print(getMode())#print it

def getMessage():
    return input("Encrypt or Decrypt")
print(getMessage())

def getKey():
    try:
        key = int(input("enter key between 1-25"))
        return key
    except:
        key = int(input("Enter key between 1-25"))
    




    
def getKey ():
    key = int(input("Enter a number betwen -25 and 25")) #asking for a key and convert to int
    while True:
        if key >=-25 and key<=25:
            return key
    else:
        key = int(input("I need a number 1-25"))
print(getKey())
'''

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
print(getTranslatedMessage("decrypt", "Uwd", 2)) # the number says how many letters to move to the right
