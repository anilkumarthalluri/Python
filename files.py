f = open("MyData","r")
#print(f.read())         #read all lines in the file

print(f.readline(), end = "")  #read the first line of a file
print(f.readline(), end = "")  #read the second line of a file

f1 = open("abc","a")        #we can pass path also
f1.write("working on files")

f.close()
f1.close()