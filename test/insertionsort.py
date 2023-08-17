def insertion_sort(arr):
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]
        
        j = i - 1
        while j>= 0 and key < arr[j]:
            arr[j +1] = arr[j]
            j-=1
        
        arr[j + 1] = key
    return arr

sample_array = [43, 65, 12, 87, 98, 56]
print("Original array: ", sample_array)

insertion_sort(sample_array)
print("Sorted Array: ", sample_array)