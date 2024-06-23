import numpy as np

arr = np.array([1+4j,2+5j,3+6j])
print("given array : ")
print(arr)

print("real part of given array : ")
x=np.real(arr)          #it returns real part of complex arguement
print(x)
#print(arr.real)

print("imaginary part of array : ")
print(np.imag(arr))     #it returns imaginary part of complex arguement
#print(arr.imag)