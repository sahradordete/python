#PRACTICE TIME
#Create a file to work with. Copy that txt file using the copy method, once it's  copied, then rename the file to another name.
import shutil
src = "testingFile.txt"
dst = "pasteText.txt"
shutil.copy(src, dst)

import os
os.rename ("pasteText.txt", "justAnotherFile")

