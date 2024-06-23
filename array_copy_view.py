import numpy as np 
print("copy():")    
arr1 = np.array([1, 2, 3, 4, 5])
x = arr1.copy()
arr1[2]=30
print(arr1)
print(x)


print("view():")
arr2 = np.array([1, 2, 3, 4, 5])
y = arr2.view()
arr2[2]=30
print(arr2)
print(y)

arr3 = np.arange(10)
print(arr3)