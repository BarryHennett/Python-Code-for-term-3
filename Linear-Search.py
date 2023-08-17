def linear_search(array, x):
    for index, element in enumerate(array):
        if element == x:
            return index
    return -1

array = [ 9, 8, 4, 5, 1, 2, 7, 4, 0]
x = 4

result = linear_search(array, x)

if result != -1:
    print("Element is present at index: " + str(result))
else:
    print("Not found")
    
    
