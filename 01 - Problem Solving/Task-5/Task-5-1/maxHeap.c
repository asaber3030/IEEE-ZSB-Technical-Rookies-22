#include <stdio.h>
#include <stdlib.h>
void swap(int *a, int *b) {
   int t;
   t  = *b;
   *b = *a;
   *a = t;
}

void heapify(int arr[], int n, int i) {

  int left = 2*i + 1;
  int right = 2*i + 2;
  int max = i;
  if (left < n && arr[left] < arr[max]) {
    max = left;
  }
  if (right < n && arr[right] < arr[max]) {
    max = right;
  }

  if (max != i) {
    swap(&arr[i], &arr[max]);
    heapify(arr, n, max);
  }
}

void buildHeap(int arr[], int n) {

  for (int i = n / 2 - 1; i >= 0; i--) {
    heapify(arr, n, i);
  }
}

void heapSort(int arr[], int n) {
  buildHeap(arr, n);
  for (int i = n - 1; i >= 0; i--) {
    swap(&arr[0], &arr[i]);
    heapify(arr, i, 0);
  }
}

void printit(int arr[], int n) {

  for (int i = 0; i < n; i++) {
    printf("%d ", arr[i]);
  }

}


int main()
{
  int array[] = {99, 92, 95, 86, 87, 81, 77, 28, 55, 51, 35, 61, 74, 57, 48, 3, 24, 15, 23, 7, 13};

  heapSort(array, sizeof(array) / sizeof(array[0]));

  printit(array, sizeof(array) / sizeof(array[0]));

  return 0;
}
