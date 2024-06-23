
print("choose an option from below : ")
print("1.Addition\n2.Substraction\n3.multiplication\n4.Division")
option = int(input("Enter your option : "))

x = int(input("Enter first number : "))
y = int(input("Enter second number : "))

def add(num1,num2):
	return num1+num2

def sub(num1,num2):
	return num1-num2


def mul(num1,num2):
	return num1*num2


def div(num1,num2):
	return num1/num2

if option == 1:
	print("sum : ",add(x,y))
elif option==2:
	print("sub : ",sub(x,y))
elif option==3:
	print("multiply : ",mul(x,y))
elif option==4:
	print("divsion : ",div(x,y))
else:
	print("invalid input")