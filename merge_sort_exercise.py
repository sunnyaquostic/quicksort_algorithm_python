def merge_sort(arr: list):
    if len(arr) <= 1:
        return
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    merge_sort(left),
    merge_sort(right)
    
    merge_two_sorted_lists(left, right, arr)
    
def merge_two_sorted_lists(a: list, b: list, arr: list):
    len_a = len(a)
    len_b = len(b)
    i = j = k =  0
    
    while i < len_a and j < len_b:
        if a[i]['time_hours'] >= b[j]['time_hours']:
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
     
    elements = [
        {'name':'vendant', 'age':17, 'time_hours': 1},
        {'name':'rajab', 'age':12, 'time_hours': 3},
        {'name':'vignesh', 'age':24, 'time_hours': 2.5},
        {'name':'chimay', 'age':21, 'time_hours': 1.5}
    ]

    merge_sort(elements)
    print(elements)