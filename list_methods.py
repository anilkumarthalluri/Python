DataList = ["Banana","Apple","Cherry","Banana","Pinapple"] #orderd,changeable,allow duplicates
print("Given List : ",DataList)

print("Length : ",len(DataList))

print("type : ",type(DataList))

newList = list((1,2,3,4,5))  #list constructor double round brackets
print("newList : ",newList)

print("index 1 : ",DataList[1])  #prints second item of list
print("index -1 : ",DataList[-1]) #prints last item of list

print("1 to 3 : ",DataList[1:3])   #prints 1 to 2

print("0 to 3",DataList[:3])         #prints from o to 2

print("2 to end : ",DataList[2:])   #prints 2 to end

print("Negative indexing : ",DataList[-3:-1])

if 'Apple' in DataList:
    print("Apple Exist..")
else:
    print("Apple Not Exist..")
    
if 'orange' in DataList:
    print("orange Exist..")
else:
    print("orange Not Exist..")
    
print("index 1: ",DataList[1])
DataList[1] = "orange"          #updating at index 1
print("After updating : ",DataList[1])
print(DataList)

DataList.insert(1,"Apple")  #inserting item at index 1
print(DataList)

DataList.append("Mango")    #adding item at last 
print(DataList)

DataList.extend(newList)    # adding newList to DataList
print(DataList)             
print("len : ",len(DataList))

thisTuple = ("hi","bye")
newList.extend(thisTuple)   # we can add list to tuple,set,dict or vice versa... 
print("newList : ",newList)

newData = ["BMW","RR","BENZ","BUGATI"]
print("newData : ",newData)
newData.remove("BMW")       #removing item with value
print("after deleting : ",newData)

newData.append("THAR")
newData.pop(1)    #removing with index 
print(newData)

del newData[1]   #removes specified index
print(newData)

newData.clear() #clear all the items in list
print(newData)

numData = [1,4,5,2,3]
print("numData : ",numData) 
numData.sort()      #sorting ascending
print("sorted numData : ",numData)
numData.sort(reverse=True)  #sorting descending
print("sorted Data : ",numData)

mylist = []
print(mylist)
mylist = numData.copy()     #copying one list to another
print(mylist)