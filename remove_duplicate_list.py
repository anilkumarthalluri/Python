myList = ['A','B','C','D','C','A']
print("List : ",myList)

newList = []
newData = []

for x in myList:
    if x not in newList:
        newList.append(x)
        newData.append(x)
        
print("After removing duplicates : ",newList)