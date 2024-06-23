MyList = [10,20,30,40,50,60,70,80,90]
print("MyList : ",MyList)
MyList.sort()
print("sorted_list : ",MyList)
num = 80
l,u = 0,len(MyList)-1

for i in range(u):
    mid = (l+u)//2
    if MyList[mid]==num:
        print("found")
        break
    else:
        if num>MyList[mid]:
            l = mid+1
        else:
            u=mid+1
else:
    print("not found")