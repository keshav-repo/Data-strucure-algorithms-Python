list = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, -2,- 2,- 2, -2]

freq = {}

for ele in list:
    if ele in freq.keys():
        freq[ele] = freq[ele]+1
    else:
        freq[ele] = 1

print(freq)

# for val, freq in freq.items():
#     print("elem {} has freq {}".format(val, freq))
#


