list = [1, 10, 5, 4, 9, 120, 4, 6, 10,6]

valueIdxDict = {}
repeatingElementIdx=len(list)+1
for i in range(0, len(list)):
    item = list[i]
    if item in valueIdxDict.keys():
        prevIdx = valueIdxDict[item]
        if repeatingElementIdx > prevIdx:
            repeatingElementIdx = prevIdx
    else:
        valueIdxDict[item] = i

print(list[repeatingElementIdx])
