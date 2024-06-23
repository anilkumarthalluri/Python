import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
print("array 1 : ")
print(arr1)

arr2 = np.array([10, 3 , 98, 20, 4])
print("array 2 : ")
print(arr2)

print("common elements : ")
print(np.intersect1d(arr1,arr2))