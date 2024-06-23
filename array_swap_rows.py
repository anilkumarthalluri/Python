import numpy as np 

arr = np.arange(1, 7).reshape(2, 3)
print("Given Array : ")
print(arr)

print("After swaping rows : ")
arr = arr[[1, 0]]
print(arr)