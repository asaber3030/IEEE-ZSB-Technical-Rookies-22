from collections import Counter

listLength = int(input().strip(' '))
birdsFreq = list(map(int, input().strip().split(' ')))

maxFrequency = max(dict(Counter(birdsFreq)), key=dict(Counter(birdsFreq)).get)

print(maxFrequency)