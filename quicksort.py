def swap(a, b, arr):
    if a != b:
        arr[a], arr[b] = arr[b], arr[a]

def partition(arr, start_pointer, end):
    pivot_index = start_pointer
    pivot = arr[pivot_index]
    
    # start_pointer = pivot_index + 1
    # end = len(arr) - 1
    
    while start_pointer < end:
        while start_pointer <= end  and arr[start_pointer] <= pivot:
            start_pointer += 1
            
        while end >= start_pointer and arr[end] > pivot:
            end -= 1
        
        if start_pointer < end:
            swap(start_pointer, end, arr)
        
    swap(pivot_index, end, arr)
    
    return end


def quick(arr: list, start_pointer, end):
    if start_pointer < end:
        pi = partition(arr, start_pointer, end)
        quick(elements, start_pointer, pi -1) #left partition
        quick(elements, pi + 1, end) #right partition



if __name__ == '__main__':
    elements = [11, 9, 29, 7, 2, 15, 28]
    testCases = [
        [11, 9, 29, 7, 2, 15, 28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]
    
    for elements in testCases:
        quick(elements, 0, (len(elements) - 1))
        print(f"sorted array: {elements} ")