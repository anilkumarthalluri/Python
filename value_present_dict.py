mydict = {1:10, 2:20, 3:30,4:40}
print("mydict : ",mydict)

x = 40

if x in mydict.values():  
    print(x,"is present")
else:
    print(x,"is not present")