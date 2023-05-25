def leftRightDifference(nums):
    leftSum = []
    for i in range(0, len(nums)):
        if i==0:
            leftSum.append(0)
        else:
            leftSum.append(leftSum[i-1]+nums[i-1])
    # print(leftSum)
    rightSum = [None]*len(nums)
    for i in range(len(nums)-1, -1, -1):
        if i == (len(nums))-1:
            rightSum[i] = 0
        else:
            rightSum[i] = rightSum[i+1]+nums[i+1]
    # print(rightSum)
    res = []
    for i in range(0, len(nums)):
        res.append(abs(leftSum[i]-rightSum[i]))
    return res


nums = [10,4,8,3]
answer = leftRightDifference(nums)
print(answer)
