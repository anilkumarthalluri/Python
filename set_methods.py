myset = {"banana","apple","orange"} #unordered,unchangable,unindexed
print("myset : ",myset)

newset = {"RR","BENZ","BMW",True,1,False,0} #True 1,False 0 considered as same - duplicates
print("newset : ",newset)

print("len : ",len(newset))

print("type : ",type(newset))

for x in newset:
    print(x," ",end="")
    
numset = {1,3,4,3,5}
print("\nnumset : ",numset)
numset.add(7)                   #adding of item to set
print("new numset : ",numset)

myset.update(numset)            #adding two sets
print(myset)

set1 = myset.union(numset)
print(set1)

numset.remove(1)        #if item does not exist error occur
print(numset)

numset.discard(10)      #if item does not exit error does occur
print(numset)

numset.clear()          #clear all the items
print("numset : ",numset)

del myset               #delete set completly