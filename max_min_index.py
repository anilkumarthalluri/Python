import numpy as np   

arr = np.array([1, 2, 3, 4, 5])
print("Original array : ")
print(arr)

print("max_index : ")
print(np.argmax(arr))   # returns array max element index 

print("min_index : ")
print(np.argmin(arr))   # returns array min element index