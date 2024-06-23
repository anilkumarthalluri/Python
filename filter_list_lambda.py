mylist = [1,2,3,4,5,6,7,8,9,10]
print(mylist)

even_list = list(filter(lambda x : x%2==0,mylist))
print("even_list : ")
print(even_list)

odd_list = list(filter(lambda x : x%2!=0,mylist))
print("odd_list : ")
print(odd_list)