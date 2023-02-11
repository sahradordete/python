#Working with While Loops
print("While Loops")
print("--------------------------------------")

a = 1
while a < 6:
    print(a)
    a += 1
print("End of the loop\n")
#\n - this jumps a line

x = "Hello World"
y = 1
while y <= 3:
    print(x)
    y += 1
print("End of the second loop")

print("----------------------------------------")
print("CONTINUE")
#This statement will check if the value equals 4 and not print it if true
x = 0
while x < 6:
    x += 1
    if x == 4:
        continue
    print(x)

print("--------------------------------------------")

#The break statement will stop the loop when a equals 4 
a = 1
while a < 14:
    print(a)
    if a == 4:
        break
    a += 1
    
