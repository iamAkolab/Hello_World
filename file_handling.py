import os

print(os.path.join('folder1','folder2','folder3'))
print(os.sep)
print(os.getcwd())

print(os.chdir(r"c:\\"))
print(os.getcwd())

#if the current working directory is bacon #
#C:\bacon\fizz\spam.txt exist
#C:\eggs\spam.txt exist


#Relative                 Absolute
#..\                      C:\ 

#..\                      C:\spam.txt 

#.\                       C:\bacon
#.\fizz                   C:\bacon\fizz
#.\fizz\spam.txt         C:\bacon\fizz\spam.txt 

#..\eggs                   C:\eggs
#..\eggs\spam.txt          C:\eggs\spam.txt 


#so it is only the reference to the current directory that
# has only one dot before the \

#absolute functions
print(os.path.abspath("dictionary.py"))
print(os.path.isabs("c:\dictionary.py"))

#relate function rgive the relative paths between 2 dir
#os.path.relpath('c:\\folder1\\folder2\\spam.png', 'c:\\folder1')
#>> 'folder2\\spam.png'

print(os.path.dirname('c:\dictionary.py'))
print(os.path.basename('c:\dictionary.py'))


print(os.path.exists('c:\\folder1\\folder2\\spam.png'))
print(os.path.isfile('c:\\windows\\system32\\calc.exe'))


print(os.path.getsize('c:\\windows\\system32\\calc.exe'))
print(os.listdir('c:\\windows\\cursors'))



totalSize = 0

for filename in os.listdir('c:\\windows\\cursors'):
    if not os.path.isfile(os.path.join('c:\\windows\\cursors', filename)):
        continue
    totalSize = totalSize + os.path.getsize((os.path.join('c:\\windows\\cursors', filename)))

print(totalSize)

#os.makedirs(c:\\delicious\\waffles\\walnut'))