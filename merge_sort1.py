import time

def merge_sort(arr: list):
    if len(arr) <= 1:
        return
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_lists(left, right, arr)

def merge_two_sorted_lists(a: list, b: list, arr: list):
    len_a = len(a)
    len_b = len(b)
    i = j = k =  0
    
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1 
         
        # Copy any remaining elements from `a`
    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1
    
    # Copy any remaining elements from `b`
    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1
     

if __name__ == '__main__':
    # a = [5,8,12,56, 100]
    # b = [7,9,45,51]
    c = [10, 3, 15, 7, 8, 23, 98, 29]
    merge_sort(c)
    print(c)
    # print(merge_two_sorted_lists(a,b))