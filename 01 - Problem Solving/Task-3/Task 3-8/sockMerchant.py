from collections import Counter


def sockMerchant(n, ar):
    s = 0
    for val in Counter(ar).values():
        s += val // 2
    return s


print(sockMerchant(10, [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]))
print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))
