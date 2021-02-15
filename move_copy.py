import shutil

#copy with same name
shutil.copy("C:\\Users\\john\\heart.txt","C:\\Users\\john\\Documents\\GitHub\\Hello-World\\heart.txt")

#copy with rename
shutil.copy("C:\\Users\\john\\heart.txt","C:\\Users\\john\\Documents\\GitHub\\Hello-World\\heartheartache.txt")

#copy folder
shutil.copytree("C:\\Users\\john","C:\\Users\\john\\Documents\\GitHub\\Hello-World")

#move with same name
shutil.move("C:\\Users\\john\\heart.txt","C:\\Users\\john\\Documents\\GitHub\\Hello-World\\heart.txt")

#move with rename
shutil.move("C:\\Users\\john\\heart.txt","C:\\Users\\john\\Documents\\GitHub\\Hello-World\\heartheartache.txt")