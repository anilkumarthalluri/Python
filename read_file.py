import os 

if os.path.exists("MyData"):
    f1 = open("MyData","r")
    print(f1.read())
else:
    print("file doesn't exist...")