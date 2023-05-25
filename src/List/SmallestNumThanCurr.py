def smallerNumbersThanCurrent(nums):
    freq = {}
    # get the frequency of each element in array
    for ele in nums:
        if ele in freq.keys():
            count = freq[ele]
            freq[ele] = freq[ele]+1
        else:
            freq[ele] = 1
    print(freq)
    #sort the keys
    keys = freq.keys()
    keys = sorted(keys)
    # store the cumulative freq
    sum = freq[keys[0]]
    freqNet = freq.copy()
    for i in range(1,len(keys)):
        key = keys[i]
        count = freq[key]
        sum = sum + count
        freqNet[key] = sum
    # add to new array
    print(freqNet)
    result = []
    for i in range(0, len(nums)):
        result.append(freqNet[nums[i]]-freq[nums[i]])
    return result

#nums = [8,1,2,2,3]
nums=[6,5,4,8]
ans = smallerNumbersThanCurrent(nums)
print(ans)
