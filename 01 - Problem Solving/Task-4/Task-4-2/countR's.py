text = input("Word: ")
textLen = input("Length: ")

repeated = text * int(textLen)
countR = repeated[:int(textLen)].count("r")

print(countR)