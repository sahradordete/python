#Create a multiple assignment operator and create 3 key/value pairs using the following as values. (Dave, 41; Bob, 22; Mark, 38). Print using an F-String. 
values = {"Dave": '41', "Bob": '22', "Mark": '38'}
for key, value in values.items():
    print(f"{key} is {value} years old")
