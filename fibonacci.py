x = int(input("Enter Range : "))

i = 0
a = 0
b = 1
c = 0
while i<=x:
    print(c," ",end="")
    a = b
    b = c
    c = a+b
    i+=1