import numpy as np   

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([1, 2, 5,4,3])
print(arr1)
print(arr2)
print(np.equal(arr1,arr2))

arr3 = np.array([ 1, 7, 13, 105])
print(arr3.size * arr3.itemsize)