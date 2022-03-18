from random import randint

randomNumber = str(randint(100, 999))

print(randomNumber)

countGuesses = 1
countHits = 0
countMisses = 0

guessedNumber = None

while guessedNumber != randomNumber:
    guessedNumber = input("Guess a number: ")

    if len(guessedNumber) < 3:
        print("You must enter a 3-digit number")

    else:

        for x in range(3):
            if guessedNumber[x] in randomNumber:
                if guessedNumber[x] == randomNumber[x]:
                    countHits += 1
            else:
                countMisses += 1
        if guessedNumber == randomNumber:
            print(f"You won! you have tried {countGuesses}")

        else:
            countGuesses += 1
            print(f"{countHits} hit {countMisses} miss!")
            countHits = 0
            countMisses = 0
