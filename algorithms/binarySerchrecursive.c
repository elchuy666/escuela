#include <stdio.h>

int binarySearch(int arr[], int low, int high, int x){
    
    if (high >= low)
    {
        int mid = low + (high +low)/2;
        if (arr[mid == x])
    {
        return mid;
    }
        if (arr[mid]<x)
        {
            binarySearch(arr, low, mid-1, high, x);
        }
        return binarySearch(arr, mid+1, high,x);
        
    }
    
    return -1;
};

//el main
int main(void)
{
    int arr[]={2,3,4,10,40};
    int n = sizeof(arr)/ sizeof(arr[0]);
    int x = 10;
    int result = binarySearch(arr,0,n-1,x);
    (result == -1) 
        ? printf("Element is not present in array"):printf("Element is preent at index %d", result);
    return 0;
}
