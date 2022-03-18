# def hackerrankInString(s):
#     word = 'hackerrank'
#     n = len(word)
#     i = 0
#     for char in s:
#         if char == word[i]:
#             i += 1
#             if i == n:
#                 return "YES"
#
#     return "NO"

def delete_f(f, k):
    l = []
    for i in f:
        while len(l) > 0 and l[-1] < i and k > 0:
            l.pop()
            k -= 1

        l.append(i)

    print(*l)




