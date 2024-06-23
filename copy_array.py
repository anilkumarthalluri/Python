from numpy import *

arr1 = array([1,2,3,4,5])
print("arr1 : ",arr1)
arr2 = arr1             #copying one way
print("arr2 : ",arr2)

arr3 = arr1.view()      #copying another way
print("arr3 : ",arr3)

arr4 = arr1.copy()      #copying another way
print("arr4 : ",arr4)   