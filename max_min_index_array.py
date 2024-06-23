import numpy as np 

arr = np.array([1, 2, 3, 4, 5])
print(arr)

x = np.argmax(arr)
print("max_index : ",x)

y = np.argmin(arr)
print("min_index : ",y)