import pandas as pd
def read_excel(filepath, col):
    dataframe = pd.read_excel(filepath, usecols= col)
    return dataframe

col = [1, 2]
filepath = 'C:\\Users\harra\Desktop\Python\SampleWork.xlsx'
dataframe = read_excel(filepath, col)
print("Data Before Sorting: ")
print(dataframe)
print(" ")
sort_data = dataframe.sort_values(by='Age')
print("Sorted Data: ")
print(sort_data)