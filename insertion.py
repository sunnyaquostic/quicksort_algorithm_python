def insertion(arr : list) -> list:

    for i in range(1, len(arr)):
        valtosort = arr[i]
        j = i - 1
        
        while j >= 0 and valtosort < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            
        arr[j+1] = valtosort
   
    return arr
        
        
# arr = [21, 38, 29, 17, 4, 25, 11, 32, 9]
arr = [2,1,5,7,2,0,5]
res = insertion(arr)
print(res)