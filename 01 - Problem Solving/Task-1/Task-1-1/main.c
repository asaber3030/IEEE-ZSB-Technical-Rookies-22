#include <stdio.h>
#include <stdlib.h>

int main()
{
    double width, length;

    printf("Enter Width: ");
    scanf("%lf", &width);

    printf("Enter Length: ");
    scanf("%lf", &length);

    if (width != 0 || length != 0) {
      printf("Area is: %f\n", width * length);
      printf("Perimeter is: %f\n", (width + length) * 2);
    } else {
      printf("None of width or length cannot be 0\n");
    }

    system("pause");

}
