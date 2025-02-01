function  merge_sort(arr) {
    if (arr.length <= 1)
        return

    let mid = Math.floor(arr.length / 2)
    let left = arr.slice(0, mid)
    let right  = arr.slice(mid, arr.length)

    merge_sort(left) 
    merge_sort(right)

    merge_two_sorted_arrays(left, right, arr)
}

function merge_two_sorted_arrays(a, b, arr) {
    let len_a  = a.length
    let len_b  = b.length

    let i = 0, j = 0, k = 0;

    while (i < len_a && j < len_b) {
        if (a[i] < b[j]) {
            arr[k] = a[i]
            i += 1
        } else {
            arr[k] = b[j]
            j += 1
        }
        k += 1
    }

    while (i < len_a ) {
        arr[k] = a[i]
        i += 1
        k += 1
    }

    while (j < len_b) {
        arr[k] = b[j]
        j += 1
        k += 1
    }
}

c = [10, 3, 15, 7, 8, 23, 98, 29]
merge_sort(c)
console.log(c)
