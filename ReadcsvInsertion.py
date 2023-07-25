import pandas as pd

def insertion_sort(arr):
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]
        
        j = i - 1
        while j>= 0 and key['Price'] < arr[j]['Price']:
            arr[j +1] = arr[j]
            j-=1
        
        arr[j + 1] = key
    return arr

def read_csv(filepath, col):
    dataframe = pd.read_csv(filepath, usecols= col)
    return dataframe

#for specific column input
col = [0, 4]

#filepaths
filepath = 'C:\\Users\harra\Desktop\Python\DiamondValues.csv'

dataframe = read_csv(filepath, col)

print("Data Before Sorting: ")
print(dataframe)
print(" ")

# Convert DataFrame to list of dictionaries to perform Insertion sort
data_list = dataframe.to_dict('records')

# Sort the data using bubble sort based on the 'Price' column
insertion_sort(data_list)

# Convert the sorted list of dictionaries back to a DataFrame
sorted_dataframe = pd.DataFrame(data_list)

print("Sorted Data: ")
print(sorted_dataframe)