list1= [11, 1, 13, 21, 3, 7]
list2 = [11, 3, 7, 1]

freq = {}
for i in range(0, len(list1)):
    ele = list1[i]
    if ele in freq.keys():
        freq[ele] = freq+1
    else:
        freq[ele] = 1

for i in range(0, len(list2)):
    ele = list2[i]
    if ele not in freq.keys():
        print("not a subset")
        break
    elif ele in freq.keys():
        freq[ele] = freq[ele]-1



