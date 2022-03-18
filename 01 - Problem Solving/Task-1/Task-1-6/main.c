#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num;
    printf("Enter a number to sum from 1 to given number: \n");
    scanf("%d", &num);
    while (!(num > 1)) {
      printf("Larger than 1 to continue \n");
      scanf("%d", &num);
    }
    int i, sum;
    sum = 0;
    for (i = 0; i <= num; i++) {
      sum += i;
    }

    printf("The sum from 1 to %d is: %d\n", num, sum);

    system("pause");
    return 0;
}
