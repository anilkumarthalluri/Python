dict1 = {
    1:"anil",
    2:"Ram",
    3:"kailash"
}
print("dict1 : ",dict1)

dict2={
    4:"ayush",
    5:"pandit"
}
print("dict2 : ",dict2)

dict3 = {
    6:'vijay',
    7:'shiva'
}
print("dict3 : ",dict3)

dict4 = {}

for x in dict1,dict2,dict3:
    dict4.update(x)
    
print(dict4)