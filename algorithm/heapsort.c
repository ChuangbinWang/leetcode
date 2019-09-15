#include <stdio.h>

void swap(int arr[],int i,int j)
{
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}

void heapAdjust(int arr[], int len, int i)
{
    int left, right, j;
    left = (i * 2 + 1);
    while(left <= len)
    {
        right = left + 1;
        j = left;
        if(right < len && arr[left] < arr[right])
        {
            j++;
        }

        if(arr[i] < arr[j])
        {
            swap(arr, i, j);
        }
        else
        {
            break;
        }
        i = j;
        left = (i * 2 + 1);
    }
}

void heapSort(int arr[], int len)
{
    for(int i = (len/2 - 1); i >= 0; i--)
    {
        heapAdjust(arr, len, i);
    }

    while (len >= 0)
    {
        /* code */
        swap(arr, 0, len--);
        heapAdjust(arr, len, 0);
    }   
}

int main()
{
    int arr[] = {20, 50,20,40,70,10,80,30,60};

    heapSort(arr, 8);
    for(int i = 0; i < 9; i++)
    {
        printf("%d \n", arr[i]);
    }
    return 0;
}