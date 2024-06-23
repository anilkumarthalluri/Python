def max_num(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c


x,y,z =input("Enter three numbers:").split(' ')
print("you entered : ",x,y,z)
print("max : ",max_num(x,y,z))