def delete_f(f, k):
    l = []
    for i in f:
        while len(l) > 0 and l[-1] < i and k > 0:
            l.pop()
            k -= 1

        l.append(i)

    print(*l)