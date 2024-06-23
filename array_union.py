import numpy as np  

arr1 = np.array([1, 2, 3, 5, 4, 7])
print("array 1 : ")
print(arr1)

arr2 = np.array([1, 2, 8, 2, 9, 10])
print("array 2 :")
print(arr2)

print("union of arr1 and arr2 : ")
print(np.union1d(arr1, arr2))