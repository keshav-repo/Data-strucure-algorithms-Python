list = [ 1, 14, 11, 51, 15]
low = 50
high = 55
present={}
for ele in list:
    present[ele]=True
for ele in range(low, high+1):
    if ele not in present.keys():
        print(ele, end=",")
