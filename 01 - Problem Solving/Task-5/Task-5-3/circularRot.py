def circularRotation(a, k, queries):
    result = []
    leng = len(queries)
    k = k % leng
    for q in queries:
        result.append(a[(leng - k + q) % leng])

    return result


print(*circularRotation([1, 2, 3], 2, [0, 1, 2]), sep='\n')
