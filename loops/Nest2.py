numbers = [1, 2, 3]
letters = ['a', 'b', 'c']

for x in numbers: #This will be executed once 
    print(x)
    for y in letters: #Then this one will be executed until it reaches its end.
        print (y)
    print("\n")

#After finishing executing the second loop the program will return to the first one and execute again ONCE.
# And so on
