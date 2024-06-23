import array

num = array.array('i',[1,2,3,5])
print(num)

for i in num:
    if i not in range(1,6):
        x = i
        print("missing : ",x)
        break