def sum_list(MyData):
    if len(MyData)==0:
        return 1
    else:
        sum = 0
        for x in MyData:
            sum = sum+x
            len(MyData)-1
    return sum
        

MyList = [3,4,5,6]
print("MyList : ",MyList)
print(sum_list(MyList))