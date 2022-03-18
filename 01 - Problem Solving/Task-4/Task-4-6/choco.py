def choco(n, c, m):
    choco = n // c  # Initially bought choco
    wrappers = choco

    while wrappers >= m:
        choco += wrappers // m
        wrappers = wrappers // m + (wrappers % m)

    return choco


print(choco(10, 2, 5))
print(choco(12, 4, 4))
print(choco(6, 2, 2))