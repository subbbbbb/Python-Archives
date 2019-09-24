binOrDec = input("Do you want to convert bintoD or DtoBin or decToHex")
if(binOrDec == "bintoD"):
    hi = input("Enter your binary number::")
    print(int(hi, 2))
elif(binOrDec == "DtoBin"):
    wassup = int(input("Enter a decimal number"))
    print(bin(wassup).replace("0b", ""))
elif(binOrDec == "decToHex"):
    wassup = int(input("Enter a decimal number"))
    print(hex(wassup).replace("0x", "").upper())
