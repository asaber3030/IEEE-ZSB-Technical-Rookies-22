#include <stdio.h>
#include <stdlib.h>

int main()
{
   /*
    * int array: The array that you want to search in
    * int findElement: The number you want to search for
    * int leftIndex: 0
    * int rightIndex: Array Length
    */

    int binarySearch(int array[], int findElement, int leftIndex, int rightIndex) {

      int midPoint = leftIndex + (rightIndex - leftIndex) / 2;

      if (leftIndex > rightIndex) {
        return -1;
      }

      if (array[midPoint] == findElement) {
        return midPoint;
      } else if (array[midPoint] > findElement) {

         return binarySearch(array, findElement, leftIndex, midPoint - 1);

      } else {
        return binarySearch(array, findElement, midPoint + 1, rightIndex);
      }

    }

    int array[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13};

    int find = 12;

    int index = binarySearch(array, find, 0, 12);

    printf("Index of %d is: %d\n", find, index);

    system("pause");

    return 0;
}
