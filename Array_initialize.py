import array as arr

num = arr.array('i',[1,2,3,4,5,5,5])
print("num : ",num)
num1 = arr.array('i',[10,20,30,40,50])
print(num1)
num.append(6)
print("append num : ",str(num))

num.reverse()
print("reverse : ",num)

print("len : ",len(num))
print("itemsize : ",num.itemsize)

print(num.buffer_info())

print(num.count(5))

num.extend(num1)

print(num)

num.insert(2,4)
print(num)