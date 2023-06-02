arr = [ 2, 1, 2, 3, 2, 1, 4, 5 ]
k = 5

for i in range(0, len(arr)-k+1):
    subList = arr[i:i+k]
    setObj = set(subList)
    print("distinct element in {} is {}".format(subList, len(setObj)))
