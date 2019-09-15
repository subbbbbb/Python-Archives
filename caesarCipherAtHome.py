def getTranslatedMessage(mode, message, key):  # translator method
    # mode is either encrypt or decrypt
    # message is the word you want translated
    # key is the number of spaces moved to the left or right
    # the ord() function takes a single character and gives the ascii value of it

    # all this does is check if it is encrypt or decrypt, mode.substring(0,1)
    if mode[0] == 'd':
        key = -key  # this switches the order and makes it so the message will be decrypted
    translated = ""  # the final word that will be printed out
    for letter in message:  # letter is the individual letter in each letter of message
        num = ord(letter)  # gets the ascii value of the letter/number
        num = num + key  # adds the key number to the ascii value
        # turns the ascii value back into a number/letter
        translated += chr(num)
    return translated  # need to add the return because this is inside a method

    # make sure the return statement is not inside the for loop


# test cases
print(getTranslatedMessage("encrypt", "helloworld!", 1))
print(getTranslatedMessage("decrypt", "ifmmpxpsme\"", 1))
