import numpy as np

arr = np.array([[1,2,3],[4,5,6]])
print("2D_Array : \n",arr)
print(arr.ndim) #prints dimensions of Array

arr1 = np.array([10,20,30],ndmin=10)
print(arr1)