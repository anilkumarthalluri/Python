import numpy as np 

arr = np.array([5, 2, 4, 3, 1])
print("Original_array : ")
print(arr)

x = np.searchsorted(arr,1)
print(x)