import numpy as np 

arr = np.arange(11)
print("Original_Array : ")
print(arr)

x = np.where(arr%2 == 0)
print("even_array : ")
print(x)

y = np.where(arr%2!=0)
print("odd_array : ")
print(y)