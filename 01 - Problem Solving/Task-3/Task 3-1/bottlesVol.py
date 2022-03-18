numberOfBottles = int(input())

caps = []
vols = 0

for i in range(numberOfBottles):

    bottleInfo = input().split()

    caps.append(int(bottleInfo[1]))

    vols += int(bottleInfo[0])

getMaxBottles = [max(caps)] # First max value of bottles capacities
caps.remove(max(caps)) # remove max value of capacities array to get the runner up value
getMaxBottles.append(max(caps)) # adding runner up value

maxCapacity = sum(getMaxBottles) # max cap

if maxCapacity > vols:
    print("Yes")
else:
    print("No")
