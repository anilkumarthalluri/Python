list1 = [1,2,53,6,3]
print("list1 : ",list1)

list2 = [1,5,53,6,1]
print("list2 : ",list2)

diff_list = list(set(list1)-set(list2))   #remove common elements 

print(diff_list)