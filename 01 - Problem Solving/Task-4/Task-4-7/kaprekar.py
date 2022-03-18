def kaprekar(p, q):
    result = []
    for i in range(p, q + 1):
        sqr = str(i ** 2)
        n = len(sqr)
        if i == 1:
            result.append(i)
        elif n > 1 and i == int(sqr[:n // 2]) + int(sqr[n // 2:]):
            result.append(i)

    if len(result) == 0:
        print('INVALID RANGE')
    else:
        for i in result:
            print(i)


kaprekar(1, 100)
