function binarySearchiterative(arr,x){
    let low = 0;
    let high = arr.length - 1;
    let mid;
    while (high >=low){
        mid = low + Math.floor((high-low)/2);

        if (arr[mid]==x){
            return mid;
        }
        if (arr[mid]>x) {
            high = mid -1;
        }
        else{
            low = mid + 1
        }
    }
    return -1;
}

function binarySearchRecursive(arr,low,high,x) {
    if (high>=low) {
        let mid = low + Math.floor((high-low)/2);

        if (arr[mid] > x) {
            binarySearchRecursive(arr, low, high-1,x);
        }

        return binarySearchRecursive(arr, mid+1, high,x);
    }
    return -1;
}