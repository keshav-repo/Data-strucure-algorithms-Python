# Convert decimal number to binary number

decimal_number=input("Please enter a decimal number ")
decimal_number=int(decimal_number)
binaryRes=""
while decimal_number!=0:
    remainder=decimal_number%2
    decimal_number = decimal_number / 2
    decimal_number = int(decimal_number)
    binaryRes = str(int(remainder)) + binaryRes

print(binaryRes)


"""
11 
5 1
2 1
1 0
0 1

"""
