#OPEN AND READ

hellofile = open('C:\\Users\\john\\Documents\\GitHub\\Hello-World\\hello.txt')
content = hellofile.read()
print(content)
hellofile.close()

hellofile1 = open('C:\\Users\\john\\Documents\\GitHub\\Hello-World\\hello_adele.txt')
content1 = hellofile1.readlines()
print(content1)
hellofile1.close()

#OPEN AND WRITE
#write mode 'w'
brekfile = open('C:\\Users\\john\\Documents\\GitHub\\Hello-World\\heart.txt','w')
brekfile.write('Don\'t break my heart')
brekfile.close()

#append mode 'a'
brekfile = open('C:\\Users\\john\\Documents\\GitHub\\Hello-World\\heart.txt','a')
brekfile.write('\n\nbecause i do not think i can love no one else')
brekfile.close()

#shelve mode
#creates 3 new files mydata.bak mydata.dat mydata.dir

import shelve

shelfFile = shelve.open('mydata')
shelfFile['cats'] = ['Zophie', 'Pooka', 'Bella','Grazt','tiger']
shelfFile.close()

shelfFile = shelve.open('mydata')
print(shelfFile['cats'])
shelfFile.close()

#dictionary type
shelfFile = shelve.open('mydata')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))

