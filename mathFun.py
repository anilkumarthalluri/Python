import math         #importing math header file
import math as m    #using alies name for math header file
from math import sqrt,pow  #importing particular function

x = math.sqrt(25)
print("square root of 25 : ",x)
x = math.sqrt(50)
print('square root of 50 : ',x)

x = math.ceil(2.2)      #round of function
print("ceil of 2 : ",x)

x = math.floor(4.8)   #round of function
print("floor of 4.8 : ",x)

x = m.sqrt(36)
print(x)

x = m.pow(3,4)
print("3**4 : ",x)

x = m.pi
print("value of PI : ",x)

x=math.sin(90)
print("sin90 : ",x)

x = math.tan(45)
print("value of tan45 : ",x)

x=math.tan(90)
print("value of tan90 : ",x)

x=min(10,20,30)
print("min : ",x)

x = max(10,20,30)
print("max : ",x)