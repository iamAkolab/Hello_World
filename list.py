list("hello")

list(range(4))

list(range(0, 100, 2))

supplies = ['staplers', 'biro', 'pencil', 'binders', 'ruler', 'marker']

for i in range(len(supplies)):
    print("Index " + str(i) + " of the supplies is " + supplies[i])

cat = ["fat","orange","loud"]
size, color, disposition = cat

size1, color1, disposition1 = "skinny", "black", "quiet"

a = "AAA"
b = "BBB"

a, b = b,a

spam = ["Ant","rat","goat","Cat", "Dog", "elephant"]

spam.append("Fox")
spam.insert(1,"bird")
spam.remove("rat")

del spam[3]

names = ["Alice","ant","Carol","Dog", "elephant"]

names.sort() #S;orted in ASCII betical order
names.sort(key = str.lower) #True Alphabetically

#strings are immutable but we can create a new list
catnames = "Zophie a cat"
newcatname = catnames[0:7] + "the" + catnames[8:12]

#Reference phenomenon
def egg(cheese):
    cheese.append("Hello")

span = [1,2,3,4,5]
egg(span)
span

#to fix
import copy

spin = [1,2,3,4,5]
cheem = copy.deepcopy(spin)

cheem[0] = "Hello"