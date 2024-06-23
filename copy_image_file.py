f1 = open("hacker.jpg","rb")    #reading binary
f2 = open("myimg.jpg","wb")     #writing binary

for i in f1:
    f2.write(i)
    
f1.close()
f2.close()