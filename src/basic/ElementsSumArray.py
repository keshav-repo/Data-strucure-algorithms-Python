def sumOfArrayElement(arr):
    sum = 0;
    for i in range(0, len(arr)):
        sum += arr[i]
    return sum

numArr = []
size = int(input("Enter a the size of array: "))

for i in range(0, size):
    inputEle = int(input("Enter element "))
    numArr.append(inputEle)

sumRes = sumOfArrayElement(numArr)
print(sumRes)
