x = int(input("Enter your age: "))
if x<18:
    raise Exception("under age")
else:
    print("permission granted")