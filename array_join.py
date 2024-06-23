import numpy as np  

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print("arr1 : ",arr1)
print("arr2 : ",arr2)

arr = np.concatenate((arr1, arr2))
print("new array : ",arr)