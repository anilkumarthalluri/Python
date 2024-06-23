import numpy as np 

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print("axis : 0 ")
arr = np.stack((arr1, arr2),axis = 0)
print(arr)

print('axis : 1')
arr = np.stack((arr1,arr2),axis=1)
print(arr)