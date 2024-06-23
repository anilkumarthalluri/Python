import numpy as np  

arr1 = np.array([1, 2, 3, 4, 5])
print("arr1 : ")
print(arr1)

arr2 = np.array([3, 4, 5, 2, 5])
print("arr2 : ")
print(arr2)

print("array difference : ")
print(np.setdiff1d(arr2,arr1))