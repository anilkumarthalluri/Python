MyList = [1, 2, 3, 4, 5]
print("MyList : ",MyList)
num = int(input("Enter number to search : "))
pos = -1
for i in MyList:
    pos = pos+1
    if (i == num):
        print(num,"found at",pos,'position')
        break
else:
    print(num,"not found in given list")