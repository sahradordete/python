#Formatting Output
salary = 44000
txt = "You make {} dollars a year"
print(txt.format(salary))

print("---------------------------------------------")
print("Multiple Curly Brackets")

string = "Dave teaches {} {}"
print(string.format("cyber", "security"))

print("----------------------------------------------")
string = "Dave loves {} {} and has {} {}."
print(string.format("cyber", "security", 14, "certifications"))

print("----------------------------------------------")
string = "David loves {1} {3} and has {2} {0}."
print(string.format("siblings", "cyber", 7, "security"))

print("-----------------------------------------------")
print("Named Indexes")
string = "Bob likes to play {act} and eat {1} {0}"
print(string.format("dogs", "hot", act="games"))

print("-----------------------------------------------")
#Another way of doing the same thing with less lines
print("A different way to do it.")
print("Bob likes to play {act} and eat {1} {0}.".format("dogs", "hot", act="games"))
