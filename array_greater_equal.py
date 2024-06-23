import numpy as np  

arr1 = np.array([1, 2, 3])
print("arr 1 : ")
print(arr1)

arr2 = np.array([2, 1, 3])
print("arr 2 : ")
print(arr2)

print("arr1 greater than arr2 or not >>>>>>")
print(np.greater(arr1, arr2))

print("arr1 is greater than or equal or not >>>>>>")
print(np.greater_equal(arr1, arr2))

print("arr1 is less than arr2 or not >>>>>>")
print(np.less(arr1, arr2))

print("arr1 is less than or equal to arr2 or not >>>>")
print(np.less_equal(arr1, arr2))