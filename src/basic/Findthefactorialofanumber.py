def Find_the_factorial(num):
    result=1
    for i in range(1,num+1):
        result=result*i
    return result






num=input("Please enter a number")
num=int(num)
Factorial=Find_the_factorial(num)
print(Factorial)









