import numpy as np 

arr = np.array([1, 2, 3, 4, 5])
print("Original_Array : ",arr)

n = int(input("Enter n value : "))
x = np.array_split(arr,n)       #splits into n arrays
print(x)

print(x[1])