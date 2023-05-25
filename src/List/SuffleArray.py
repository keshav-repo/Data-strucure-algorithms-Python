def shuffle( nums, n):
    res = []
    for i in range(0, n):
        res.append(nums[i])
        res.append(nums[i+n])
    return res

nums = [2,5,1,3,4,7]
n = 3

res = shuffle(nums, n)
print(res)

