import MyModule as cal

x,y = input("Enter two numbers : ").split(' ')

a,b=int(x),int(y)

print("sum : ",cal.add(a,b))
print("difference : ",cal.sub(a,b))
print("multiply : ",cal.mul(a,b))
print("division : ",cal.div(a,b))