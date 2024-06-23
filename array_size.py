import numpy as np  

arr = np.array([1, 2, 3, 4, 5])
print("given array : ")
print(arr)

print("size of array : ")
print(arr.size)         # returns size of array

print("size of each element : ")
print(arr.itemsize)     # returns size of element of array

print("space occupied by array : ")
#print(arr.size * arr.itemsize)
print(arr.nbytes)       #return space occupied by array