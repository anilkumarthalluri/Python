mydict = {1:"Anil",                     #ordered,changeable,not allow duplicatees
          2:"tyson",
          3:"Ram",
          4:"Ayush",
          3:"pandit"
          }  
print("mydict : ",mydict)

print("length : ",len(mydict))          #length

print("type : ",type(mydict))           #type

print("key 2 : ",mydict[2])             #accesing items using key

print("key 4 : ",mydict.get(4))         #accesing using get()

print(mydict.keys())                    #prints all the keys

print(mydict.values())                  #prints all the values

mydict.update({3:"RR"})                 #updating 
print("After updating : ",mydict)        

mydict.pop(1)                           #deleting using key                 
print("using pop : ",mydict)  

mydict.popitem()                        #removing last item
print("popitem : ",mydict)

del mydict[2]
print("using del : ",mydict)

mydict.clear()
print(mydict)

# del mydict
# print(mydict)                       #error because delete dictionry 

newdict = {
    "Anil" : 90,
    "Ram"  : 98,
    "wariko":70,
    "Teja"  :94
}
print("newdict : ",newdict)

for x in newdict:               #prints keys only
    print(x,"",end="")
    
for x in newdict:               #prints values only
    print(newdict[x])
    
for x in newdict.keys():
    print(x)
    
for x in newdict.values():
    print(x,"",end="")
    
extradict = newdict.copy()
print("\nextradict : ",extradict)