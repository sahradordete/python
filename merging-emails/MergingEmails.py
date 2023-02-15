#Module 17 - Merging Emails
with open("Names.txt", "r") as namefile:
    with open("Message.txt", "r") as messagefile:
        body = messagefile.read()
        for name in namefile:
            mail = "Hello " + name + body
            with open(name.strip() + ".txt", "w") as messagefile: #This will create a txt file invitation to each name in the list 
                messagefile.write(mail)

with open("Sara.txt", "r") as saras:
    print(saras.read())
