function bubble_sort(arr) {
    for (i = 0; i <= arr.length - 1; i++) {
        for (j = 0; j <= (arr.length - i - 2); j++) {
            if(arr[j] > arr[j + 1]){
                temp = arr[j]
                arr[j] =  arr[j+1]
                arr[j+1] =  temp
            }
        }
    }
    
    return arr;
}

arr = [5, 6, 3, 2, 4, 9]
const res = bubble_sort(arr)
console.log(res);
