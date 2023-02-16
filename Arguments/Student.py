#Using Default Arguments

def student(firstname, lastname="Bigger", major="Information Technology"):
    print(firstname, lastname, "majors in", major)

print("1 argument")
student("Tony")
print("------------------------------------------------------------------")

print("3 arguments")
student("Tony", "Stark", "Physics")
print("------------------------------------------------------------------")

print("2 arguments")
student("Stan", "Lee")
