# before writing the code, write the dictionary converter, from a to z and so on
alphabet_convert = {'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V',
                    'F': 'U', 'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q',
                    'K': 'P', 'L': 'O', 'M': 'N', 'N': 'M', 'O': 'L',
                    'P': 'K', 'Q': 'J', 'R': 'I', 'S': 'H', 'T': 'G',
                    'U': 'F', 'V': 'E', 'W': 'D', 'X': 'C', 'Y': 'B', 'Z': 'A', " ": " "}

print("Welcome to the atBash cipher program")
# use .upper() or .lower() depending on the dictionary
message = (input("Enter a message that you want to encrypt::")).upper()
answer = ""
for letter in message:
    # make a new variable and then use the x[y] to convert
    answer += alphabet_convert[letter]
print(answer)  # print the answer outside of the for loop

# Comments
# before writing the code, write the dictionary converter, from a to z and so on
# use .upper() or .lower() depending on the dictionary
# make a new variable and then use the x[y] to convert
# print the answer outside of the for loop
# make sure to have the print statement outside
