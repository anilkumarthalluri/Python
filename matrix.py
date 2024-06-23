from numpy import *

arr1 = array([
    [1,2,3,4],[5,6,7,8]
])
print(arr1)

m = matrix(arr1)
print(m)

a = matrix('1 2 3; 4 5 6; 7 8 9')
b = matrix('9 8 7; 6 5 4; 3 2 1')
c = a+b             #adding two matrix
print("a+b : ",c)      
print("a*b : ",a*b)     #multiplying two matrix