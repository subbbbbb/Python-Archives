binOrDec = input("Do you want to convert bintoD or DtoBin")
if(binOrDec == "bintoD"):
    hi = input("Enter your binary number::")
    print(int(hi, 2))
elif(binOrDec == "DtoBin"):
	wassup = int(input("Enter a decimal number"))
	print(bin(wassup).replace("0b", ""))
