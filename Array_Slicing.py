import numpy as np      

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(arr[1:10:2])
print(arr[:6])
print(arr[6:])
print(arr[::2])

arr1 = np.array([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10]])
print(arr1[1,1:4])
print(arr1[0,:5])