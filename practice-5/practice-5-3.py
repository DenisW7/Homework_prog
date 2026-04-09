def selection_sort(arr):
    if arr is None:
        return []
    
    result = arr.copy()
    n = len(result)
    
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if result[j] < result[min_index]:
                min_index = j
        if min_index != i:
            result[i], result[min_index] = result[min_index], result[i]
    
    return result