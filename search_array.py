import numpy as np  

arr = np.array([4, 1, 4, 2, 3, 4, 5, 4, 4])
print("Original_array : ",arr)

x = np.where(arr==4)
print(x)