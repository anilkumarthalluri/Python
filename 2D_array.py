from numpy import *

arr1 = array([
    [1,2,3], [4,5,6],[7,8,9]
])
print("arr1 : ",arr1)

print("size : ",arr1.size)      #size of array

print("shape : ",arr1.shape)    #return rows,columns

print("flatten : ",arr1.flatten())      #converts 2d to 1d

print(arr1.reshape(3,3))        #converts 1d to 2d or 3d