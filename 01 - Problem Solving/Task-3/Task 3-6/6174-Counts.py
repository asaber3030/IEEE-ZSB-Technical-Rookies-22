a = int("".join(sorted([i for i in str(input())])))
b = int("".join(sorted([i for i in str(a)], reverse=True)))

cc = ''

count = 0

if int(a) > int(b):
    b, a = a, b

print(a)
print(b)
if len(str(a)) == 4:
    while True:
        target = int(b) - int(a)
        if len(str(target)) <= 3:
            target = str(target) + "0"
        b = sorted(str(target))
        for i in b:
            cc += i
        b = cc[::-1]
        a = b[::-1]
        cc = ''
        count += 1
        if target == 6174:
            break
    print(count)
else:
    print('Enter 4 digit number')
