num = [1,2,3,4,5,6,7,8]
print("original list: ",num)

even  = list(filter(lambda n: n%2==0,num))
print(even)