list1=[42,3,40,51,36]
max=list1[0]
for i in range(0,len(list1)):
    if list1[i]>max:
        max=list1[i]

print(max)