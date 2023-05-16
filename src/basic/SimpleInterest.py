#  simple interest p, r, t

def findSimpleInterest(principal, rate, time):
    interest = principal * rate * time / 100;
    return interest

principal = int(input("Enter the priciapl amount "))
time = int(input("Enter the time "))
rate = float(input("enter the rate"))

interestCalculated = findSimpleInterest(principal, rate, time)

print("interes is "+str(interestCalculated))
