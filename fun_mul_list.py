def mul_list(list1):
    count = 1
    for x in list1:
        count = count*x
    return count

list1 = [1,2,3,4,5]
print("list1 : ",list1)
print("mul_list : ",mul_list(list1))