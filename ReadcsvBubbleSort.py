import pandas as pd
#bubble sort code to sort the price
def bubble_sort(arr):
    n = len(arr)
        
    for i in range(n - 1):
        
        for DV in range(0, n - i - 1):
            
            if arr[DV]['Price'] > arr[DV+ 1]['Price']:
                arr[DV], arr[DV +1] = arr[DV + 1], arr[DV]
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

# Convert DataFrame to list of dictionaries to perform bubble sort
data_list = dataframe.to_dict('records')

# Sort the data using bubble sort based on the 'Price' column
bubble_sort(data_list)

# Convert the sorted list of dictionaries back to a DataFrame
sorted_dataframe = pd.DataFrame(data_list)

print("Sorted Data: ")
print(sorted_dataframe)