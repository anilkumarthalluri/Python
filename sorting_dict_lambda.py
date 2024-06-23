mylist = [
    {"no" : "1", 2 : "Raghav", "name" : "keshav"},
    {"no" : "2", 4 : "pandit", "name" : "rahul"},
    {"no" : "3", 8 : "tharun", "name" : "navin"}
]
print("origina_list : ",mylist)

sorted_list = sorted(mylist,key=lambda a : a["no"])
print(sorted_list)