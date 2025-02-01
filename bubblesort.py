# is most inefficient sorting algorithm
def sorting_algo(arr: list) -> list:
    
    countLen = len(arr)
    
    for x in range(countLen):
        for j in range(countLen-x-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1], arr[j]

    return arr
    
arr = [8, 9, 4 ,3, 6]
ans = sorting_algo(arr)
print(ans)