import numpy as np   

arr = np.array([1, 2, 3])
print("Original array : ")
print(arr)

n = int(input("Enter number to repeat element : "))
print("array element repeating",n,"times : ")
print(arr.repeat(n))        #repeating each element by n times

print("array repeating",n,"times : ")
print(np.tile(arr,n))       # repeating array by n times 