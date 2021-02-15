import os


#delete
print(os.getcwd())
os.unlink()

#delete folder, folder must be empty
os.rmdir("C:\\Users\\john\\heart.txt")

import shutil

#delete folder, everything is deleted be careful!!!
shutil.rmtree("C:\\Users\\ai")

#before deleting always print out the file name to be sure

os.chdir("C:\\Users\\john\\desktop")

for filename in os.listdir():
    if filename.endswith('.txt'):
        #os.unlink(filename)
        print(filename)