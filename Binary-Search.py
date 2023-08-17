def binarySearch(Element, x, low, high):

    while low <= high:
        
        mid = low + (high - low)//2
        
        if Element[mid] == x:
            return mid
        
        elif Element[mid] < x:
            low = mid + 1
            
        else:
            high = mid -1
            
    return -1


Element = [ 3, 4, 5, 6, 7, 8, 9]
x = 4

Final = binarySearch(Element, x, 0, len(Element)-1)

if Final != -1:
    print("Element is present at index: " + str(Final))
else:
    print("Element is not found")