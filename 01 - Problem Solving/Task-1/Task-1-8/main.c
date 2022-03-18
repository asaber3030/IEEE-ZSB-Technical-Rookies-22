#include <stdio.h>
#include <stdlib.h>

int main()
{
    srand(time(NULL));

    int tries = 1;

    int randomNumber = ( rand() %  10 ) + 1;

    int guessedNumber;

    printf("Guess a number between 1 and 10: ");

    scanf("%d", &guessedNumber);

    while (guessedNumber != randomNumber) {
        printf("Try again!\n");
        printf("Guess a number between 1 and 10: ");
        scanf("%d", &guessedNumber);
        tries++;
    }
    if (guessedNumber == randomNumber) {
        printf("You won!\n");
        printf("You tried %d times\n", tries);
        system("pause");
    }

    system("pause");

    return 0;
}
