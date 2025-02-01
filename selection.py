def selection_sort(arr: list) -> list:
    for i in range(len(arr)) :
        min_value = arr[i]
        min_index = i
        
        for j in range(len(arr)):
            if arr[j] > min_value:
                min_value = arr[j]
                min_index = j
                
                arr[i], arr[j] = arr[j], arr[i]
                
    return arr
        
        
        
        
arr = [5, 3, 6, 2, 1, 8]
res = selection_sort(arr)
print(res)
