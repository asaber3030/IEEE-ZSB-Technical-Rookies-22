userWord = input("Enter A Word Or Number: ")
wordLen = len(userWord)
revStr = userWord[wordLen::-1]

if revStr == userWord:
    print("yes")
else:
    print("no")
