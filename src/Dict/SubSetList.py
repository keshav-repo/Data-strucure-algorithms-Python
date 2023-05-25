list1= [11, 1, 13, 11, 1, 1]
list2 = [11, 13, 1,7]

freq = {}
for i in range(0, len(list1)):
    ele = list1[i]
    if ele in freq.keys():
        freq[ele] = freq[ele]+1
    else:
        freq[ele] = 1

isSubset=True
for i in range(0, len(list2)):
    ele = list2[i]
    if ele not in freq.keys():
        isSubset = False
        break
    elif ele in freq.keys():
        freq[ele] = freq[ele]-1

if isSubset == True:
    print("list 2 is subset of list 1")
else:
    print("list 2 is not subset of list 1")

