def breakingRecords(scores):
    minVal = maxVal = scores[0]
    maxRecord = minRecord = 0
    for i in scores[1:]:

        if i > maxVal:
            maxRecord += 1
            maxVal = i

        elif i < minVal:
            minRecord += 1
            minVal = i

    return maxRecord, minRecord


print(breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1])) # output: (2, 4)
print(breakingRecords([3, 4, 21, 36, 10, 28, 35, 5, 24, 42])) # output: (4, 0)
