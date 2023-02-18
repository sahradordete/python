#Display Working Directory

import os
dirpath = os.getcwd() #This will show the full path
print("Your current directory is :" + dirpath)
foldername = os.path.basename(dirpath)
print("The directoy name is " + foldername)
