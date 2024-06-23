import numpy as np 

arr = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
print("Given Array : ")
print(arr)

print(np.mean(arr,axis=0))   #axis represent dimension axis=0 column axis = 1 row