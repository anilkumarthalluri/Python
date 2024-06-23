import numpy as np   

arr = np.array([1,2,np.nan,np.inf])  #not a number ,positive infinity
print(np.isfinite(arr))

arr1 = np.array([1,2,3,4])
print(np.isfinite(arr1))        #checking elements are finite or not

print(np.isinf(arr))            #checking elements are infinite or not