a = 10
b = 0
try:
    print(a/b)
    
except Exception as e:
    print("can't divide by zero",e)
    
finally:
    print("operation is over...")