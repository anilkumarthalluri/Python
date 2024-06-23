import numpy as np 

arr = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
print("Original Array : ")
print(arr)

print("iterating through for loop : ")
for x in arr:
    print(x)
    
print("iterating each and every element : ")
for x in arr:
    for y in x:
        print(y)
        
print("iterating through nditer() :")
for x in np.nditer(arr):
    print(x)