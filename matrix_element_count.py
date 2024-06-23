import numpy as np 

arr = np.array([1, 2, 3, 2, 3, 2, 3, 2, 2])
x = np.count_nonzero(arr==2)        #returns occurence of value
print(x)