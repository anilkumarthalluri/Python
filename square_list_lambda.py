
mylist = [1, 2, 3, 4, 5]
print("original_list : ",mylist)

double_list = list(map(lambda x : x**2,mylist))
print("square : ",double_list)

triple_list  = list(map(lambda x : x**3,mylist))
print("triple : ",triple_list)