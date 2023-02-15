#Reading Files

print("-----------------------------------------")
print("Reading Files - With")

with open ("demo.txt") as myfile:
    contents = myfile.read()
    print(contents)

a = open("demo.txt", "a") #a means append
a.write("\nHere is another line in our text file") #This is appending this text to the end of the document
a.close()

print("-----------------------------------------")
#Below we are opening our file again to check what it shows after appending the line above.
with open("demo.txt") as myfile:
    contents = myfile.read()
    print(contents)
#If I keep running this it will continue appending the new line to the document over and over

print("Using w to write in a file")

a = open("demo.txt", "w")
a.write("What has happened now?") #This will overwrite my demo.txt file
a.close()

print("----------------------------")

with open("demo.txt") as myfile:
    contents = myfile.read()
    print(contents)

print("----------------------------------------------------")
#How to create a file
y = open("SahraFile.txt", "x")
    
