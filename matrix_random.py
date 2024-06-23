import numpy as np 

arr = np.random.random(9).reshape(3, 3)
print("Given Array : ")
print(arr)

arr[arr>0.5]=1
arr[arr<=0.5]=0
        
print(arr)