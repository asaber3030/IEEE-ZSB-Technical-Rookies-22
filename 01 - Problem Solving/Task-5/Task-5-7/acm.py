def acmTeam(topic):
    maxSubject = 0
    length = 0

    for i in range(n):
        for j in range(i, n):
            sub = 0
            for x, y in zip(topic[i], topic[j]):
                if x == '1' or y == '1':
                    sub += 1

            if sub > maxSubject:
                maxSubject = sub
                count = 1
            elif sub == maxSubject:
                count += 1

    return [maxSubject, count]
