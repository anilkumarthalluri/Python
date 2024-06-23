#we can initialize array with importing array module
import array 

num = array.array('i',[1,2,3,4,5])
print(num)

for x in num:
    print(x,'',end="")
    
print()
# or we can initialize array with using list
myarray = [1,3,4,2,5]
print(myarray)
