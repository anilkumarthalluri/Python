import array as arr

num = arr.array('i',[1,1,2,3,3,4,4,4,5,5,5])
print("original_array : ",num)

num1 = list(set(num))
print("distinct_array : ",num1)