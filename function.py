def demo():
    print("Hey, Anil")
    
demo()

def add_sub(x,y):
    a = x+y
    b = x-y
    return a,b

x,y = add_sub(10,20)
print(x,y)

def sum(*a):
    print(a)

sum(1,2,3,4,5)

def person(name,**data):        #keyword variable length arguement
    print(name)
    print(data)
    
person("Anil",city='HYD',mob=1234)