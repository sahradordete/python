#Using the coding in this module, create a new file, write some text to the file and then read and print to the screen.

#First step: create and write in the file
file = open("myfile1.txt", "x")
file.write("Please write this on my file!")
file.close()

#Second step: read and print what was written in the file 
with open ("myfile1.txt") as myfile:
    contents = myfile.read()
    print(contents)

    
