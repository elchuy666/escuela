 #include <stdio.h>

 int binarySearch(int arr[], int low, int high,int x){

    while (low <= high)
    {
        int mid = low +(high-low)/2;

        //checar si x esta en el medio
        if (arr[mid] == x)
        {
            return mid;
        };
        if (arr[x]<mid)
        {
            low = mid+1;
        }
        else
        high = mid-1;
        
        
    }
    return -1;
    
 }

 int main(void)
 {
    int arr[]= {2,3,4,10,40};
    int n = sizeof(arr) / sizeof(arr[0]);
    int x = 10;
    int resultado = binarySearch(arr, 0, n-1, x);
    (resultado == -1) ? printf("Elemento no presente"): printf("elemento presente en ""index %d",resultado);

    return 0;
 }
 
