#Create a new txt file using python, write some lines of text to that file. Then copy that txt file using the copy method to another file name.
#Append some lines to the copied file. Print both txt files to the screen to compare. 


#y = open("newFile.txt", "x")

import shutil
src = "newFile.txt"
dst = "nowfile.txt"
shutil.copy(src, dst)

myWriting = open("nowfile.txt", "a")
myWriting.write("\nThis is my second file.")
myWriting.close()

show = open("newFile.txt", "r")
print(show.read())
show.close()

print("------------------------------------------------------------------")

secondfile = open("nowfile.txt", "r")
print(secondfile.read())
secondfile.close()
