print("hey, Anil")  #we can use double quotes

x = 'hi'            #we can use single quotes
print(x)
print(x[1])         #accesing through index

b = '''
    lorem
    fdkjf
    fjdifji
    fidjfi
'''
print(b)

c = """
fkjdf
fjdkfd
fjfkdfj
ffjdf
"""
print(c)

for i in x:
    print(i,end="")
    
print("len(x) : ",len(x))

txt = "  PYthon iS easy tO lEaRn "
print(txt)
print("python" in txt)
print("Python" in txt)

print(txt[2:9])

print(txt.upper())      #converts into uppercase
print(txt.lower())      #converts into lowercase

print(txt.strip())      #removes white spaces

mytxt = "hello,world!"
print("mytxt : ",mytxt)
a=mytxt.replace('h','H')        #replacing
print(a)

print(mytxt.split(','))         #spliting into two parts

a = "hi"
b = "anil"
print(a)
print(b)
c = a+" " +b          #string concatenation
print(c)

age = 20             #we can't combine num and string 
msg = "I am {} years old"       # we can combine using format fun
print(msg.format(age))