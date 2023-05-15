def isPrime(num):
    if num == 1:
        return False
    elif num > 1:
        for i in range(2, int(num / 2)):
            if (num % i) == 0:
                return False
        return True


# Get input from user
num = int(input("Enter a number: "))

if (isPrime(num)):
    print(str(num) + " is prime")
else:
    print(str(num) + " is not a prime")
