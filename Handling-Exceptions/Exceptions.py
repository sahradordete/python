#Handling Exceptions

try:
    print(0/0)
except ZeroDivisionError: #This will trap errors
    print("You can't divide by zero!")

print("---------------------------------------------")

import sys
try:
    num = int(input("Enter a number between 1-10"))
except ValueError:
    print("Please use numbers only")
    sys.exit()
print("You entered the number:", num)
   
