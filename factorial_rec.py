def fact(x):
    count = 1
    if x == 0:
        return 1
    else:
        count = x*fact(x-1)
    return count

x = int(input("Enter number : "))
if x<0:
    print("no factorial for negative number")
elif x==0:
    print("factorial : ",1)
else:
    print(fact(x))