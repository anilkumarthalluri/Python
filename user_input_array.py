import array 

num = array.array('i',[])
print(num)

n = int(input("Enter range of Array : "))

for x in range(n):
    x = int(input("Enter value : "))
    num.append(x)
    
print(num)

if 1 in num:
    print("present")
else:
    print("not present")