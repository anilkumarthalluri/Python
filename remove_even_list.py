myList = [1,5,4,3,2,10,13,99,9,6,7]
print("myList : ",myList)

for x in myList:
    if x%2==0:
        myList.remove(x)

print("odd list : ",myList)