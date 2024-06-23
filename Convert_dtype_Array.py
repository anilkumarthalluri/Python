import numpy as np   

arr = np.array([1,2,3.6,4.5])
arr1 = arr.astype('i')    #arr.astype(int)
print(arr1)

arr2 = np.array([1,0,4,2.0])
newarr = arr2.astype(bool) #arr2.astype('b')
print(newarr)