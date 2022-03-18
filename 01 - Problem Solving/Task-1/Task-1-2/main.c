#include <stdio.h>
#include <stdlib.h>

int main()
{

  /*
   * Task Description: Print prime numbers from 1 to the given number
   * Required: n > 1
   * n -> int stopAt
   */


  int stopAt, isPrime, j, i;

  printf("Enter a number: ");
  scanf("%d", &stopAt);


  if (stopAt > 1) {


    for (i = 2; i <= stopAt; i++) {

      isPrime = 1;

      for (j = 2; j <= i/2; j++) {

        if (i % j == 0) {
          isPrime = 0;
          break;
        }

      }

      if (isPrime == 1) {
        printf("%d ", i);
      }

    }
    printf("\n");

  } else {
    printf("\nTry again!");
  }


  system("pause");

  return 0;
}
