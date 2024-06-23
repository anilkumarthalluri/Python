mydict = {1:10, 2:20, 3:30,4:40}
print("mydict : ",mydict)

x = 4

if x in mydict.keys():  #if x in mydict:
    print(x,"is present")
else:
    print(x,"is not present")