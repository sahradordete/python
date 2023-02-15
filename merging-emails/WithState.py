#With Practice

with open("Hello.txt", "w") as file: #This will create the file and enable writing
    file.write("Hey there!")

x = open("Hello.txt", "r")
print(x.read())
x.close()
