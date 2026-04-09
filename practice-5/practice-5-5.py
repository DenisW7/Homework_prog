def insertion_sort(arr):
    if not arr:
        return []
    
    result = arr.copy()
    n = len(result)
    
    for i in range(1, n):
        key = result[i]
        j = i - 1
        
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        
        result[j + 1] = key
    
    return result