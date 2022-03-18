def findDigits(num):

    count = 0
    for i in str(num):
        if int(i) != 0 and num % int(i) == 0:
            count += 1

    return count


print(findDigits(1012))