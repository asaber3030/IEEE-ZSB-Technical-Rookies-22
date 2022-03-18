def kangaroo(x1, v1, x2, v2):
    if x1 < x2 and v1 < v2:
        return "NO"

    else:
        if v1 != v2 and (x2 - x1) % (v1 - v2) == 0:
            return "YES"
        else:
            return "NO"


x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(x2), int(v1), int(v2)]

print(kangaroo(x1, v1, x2, v2))