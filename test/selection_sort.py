def Selection_sort(arr, size):
    
    for step in range(size):
        min_idx = step
        
        for i in range(step + 1, size):
            
            if arr[i] < arr[min_idx]:
                min_idx = i
        
        (arr[step], arr[min_idx]) = (arr[min_idx], arr[step])
    return arr

data = [-2, 45, 0, 11, -9]
size = len(data)
Selection_sort(data, size)
print('Sorted Array in Ascending Order:')
print(data)