from numpy import *

num1 = array([1, 2, 3, 4, 5.0])     #array()-creating array
print("num : ",num1)

num2 = linspace(0,15,7)             #linspace()-creating array with parts
print("num2 : ",num2)

num3 = arange(1,15,5)               #arange()-creating array with skipping values
print("num3 : ",num3)

num4 = zeros(5,int)                 #zeros()-creating array with zero
print("num4 : ",num4)

num5 = ones(5,int)                  #ones()-creating array with ones
print("num5 : ",num5)
