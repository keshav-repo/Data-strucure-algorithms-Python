"""
Write a program to check even or odd number
"""

def isEven(num):
   if(num%2==0):
      return True
   else:
      return False

# Get input from user
num = int(input("Enter a number: "))

if (isEven(num)):
   print(str(num)+ " is even")
else:
   print(str(num) + " is odd")
