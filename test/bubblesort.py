def bubble_sort(arr):
    n = len(arr)
        
    for i in range(n):
        
        for Borg in range(0, n-i-1):
            
            if arr[Borg] > arr[Borg+ 1]:
                arr[Borg], arr[Borg +1] = arr[Borg + 1], arr[Borg]
                
                
         
Hamber = [34, 54, 12, 9, 45, 87, -9]
print("Orriginal Array: ", Hamber)
                
bubble_sort(Hamber)
print("Sorted Array: ", Hamber)