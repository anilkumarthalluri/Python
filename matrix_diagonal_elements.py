import numpy as np 

arr = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
print("Given Array : ")
print(arr)


diag_elements = np.diag(arr)    #it returns diagonal elements of array
print("diagonal elements : ")
print(diag_elements)

print("mean of diag_elements : ")
print(np.mean(diag_elements))      #mean of diagonal elements