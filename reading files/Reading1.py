a = open("demo.txt", "r")
print(a.read())

print("----------------------------------------")
print("Reading Files - Readline()")
print(a.readline())
a.close()

print("-----------------------------------------")
a = open("demo.txt", "r")
print(a.read(3))
a.close()

print("-----------------------------------------")
print("Reading Files - With")

with open ("demo.txt") as myfile:
    contents = myfile.read()
    print(contents)
