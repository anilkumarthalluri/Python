data = ['abc','xyz','aba','1221']
print("list : ",data)

count = 0
for x in data: 
    if len(x)>=2 and x[0] == x[-1] :
       count+=1
       
print("result : ",count) 