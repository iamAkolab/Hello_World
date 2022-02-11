# create a dictiona
myPc = {"size": 14, "color":"silver", "os":"windows10"}

# get value by key
myPc["os"]

# use the get value in print
print("My laptop has " + myPc["color"] + " color")

# Order matter for list
print([1,2,3] == [3,2,1])

# Order does not matter for dictionary
myPc1 = {"size": 14, "color":"silver", "os":"windows10"}
myPc2 = { "os":"windows10", "size": 14, "color":"silver"}

# print binary output
print(myPc1 == myPc2)

# print color
print("color" in myPc1)

# Dictionary functions
print(list(myPc1.keys()))

print(list(myPc1.values()))

print(list(myPc1.items()))

for k in myPc1.keys():
    print(k)

for j in myPc1.values():
    print(j)

for k,v in myPc1.items():
    print(k,v)

# Get methods: to prevent KeyError when the key does not exist
myPc2.get("os","")

print(myPc2.get("siz",15))

# SetDefault: set default value if it does not exist 
myPc2.setdefault("maker","Dell")
print(myPc2)
myPc2.setdefault("maker","hp")
print(myPc2)   ## remains Dell