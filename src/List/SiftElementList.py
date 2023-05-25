list=[1,2,3,4,5]

size = len(list)
temp = list[size-1]
for i in range(size-1, 0,-1):
    list[i] = list[i-1];
list[0] = temp

print(list)
