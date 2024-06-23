num = {
    1:10,
    2:20,
    3:30
}
print("num : ",num)

color = {
    4:"Red",
    5:"orange",
    6:"blue"
}
print("color : ",color)

newdict = num.copy()
newdict.update(color)
print(newdict)