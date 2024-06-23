import numpy as np 

arr = np.array([1, 2, 3,"tyson"])
print(arr)

for x,y in np.ndenumerate(arr):
    print(x,y)