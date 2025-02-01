function selection_sort(arr) {
    let minValue;
    let minIndex;

    for (i = 0; i<=arr.length - 1; i++) {
        minValue = arr[i]
        minIndex = i

        for (let j = 0; j < arr.length - 1; j++) {
            if (arr[j] > minValue) {
                minValue = arr[j]
                minIndex = j

                arr[j] = arr[i]
                arr[i] = minValue
            }
        }
    }

    return arr
}

arr = [6 ,7, 3, 2, 5,4, 1]
res = selection_sort(arr)
console.log(res)