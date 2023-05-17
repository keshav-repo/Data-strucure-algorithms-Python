decimal_number=input("Please enter a decimal number ")
decimal_number=int(decimal_number)
binaryRes=""
while decimal_number>=1:
    remainder=decimal_number%2
    decimal_number = decimal_number / 2
    decimal_number = int(decimal_number)
    if(decimal_number!=1):
        binaryRes = str(int(remainder)) + binaryRes

print(binaryRes)
