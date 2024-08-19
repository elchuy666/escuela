public class binarySearch {
    //Return index of x if it is present in arr[l...r] else return -1
int search(int arr[], int l, int r, int x)
    {
        while (l <= r) {
            int mid = (l + r) / 2;

            //if the element is present at the 
            //middle 
            if (arr[mid] == x) {
                return mid;
 
            // If element is smaller than mid, then
            // it can only be present in left subarray
            // so we decrease our r pointer to mid - 1 
            } else if (arr[mid] > x) {
                r = mid - 1;
 
            // Else the element can only be present
            // in right subarray
            // so we increase our l pointer to mid + 1
            } else {
              l = mid + 1;
            }  

        }
        return -1;
        }
        public static void main(String[] args) {
            binarySearch ob = new binarySearch();

            int arr[]= {1,2,3,4,5,10,40};
            int n = arr.length;
            int x = 10;
            int result = ob.search(arr,0,n-1,x);
            if (result == -1) {
                System.out.println("Element is not present");
            }else{
                System.out.println("Element found at index" + result);
            }
        }
}


