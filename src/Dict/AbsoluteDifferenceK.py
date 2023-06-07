nums = [1,2,2,1]
k = 1
counter = 0
for i in range(0, len(nums)):
    numi = nums[i]
    for j in range(i+1, len(nums)):
        numj = nums[j]
        if abs(numi-numj)==k:
           counter = counter +1
           #print("idx: {} {}".format(i, j))

print(counter)
