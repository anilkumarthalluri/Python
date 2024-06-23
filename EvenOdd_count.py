print("given list : ")
for i in range(1,10):
    print(i," ",end=" ")

ecount=ocount=0
for i in range(1,10):
    if(i%2==0):
        ecount+=1
    else:
        ocount+=1

print()
print("even numbers : ",ecount)
print("odd numbers : ",ocount)