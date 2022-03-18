string = input("Enter a string: ")

sub_string = input("Enter a sub string: ")

lenStr = len(string)
lenSub = len(sub_string)

counter = 0

for i in range(lenStr - lenSub + 1):

    if string[i:(i + lenSub)] == sub_string:
        counter = counter + 1

print(counter)