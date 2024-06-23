myList = [1,4,3,2,5]
print("myList : ",myList)

count=0
for x in myList:
    if x in myList:
        count+=1
    
if count == 0:
    print("myList is Empty")
else:
    print("myList is not empty")

newList = [10,20,39,40,50]
print("newList : ",newList)
if not myList:
    print("newList is empty")
else:
    print("newList is not empty")

newData = []
print("newData : ",newData)
if not newData:
    print("newData is empty")
else:
    print("newDaa is not empty")