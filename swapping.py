a = 10
b = 20
print("a  b :  ",a,b)

temp = a
a = b
b = temp
print("After swaping ")
print("a b : ",a,b)

a,b = b,a
print("a b : ",a,b)

a = a+b
b = a-b
a = a-b
print("a b : ",a,b)