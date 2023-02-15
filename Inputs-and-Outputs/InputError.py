#Trapping for errors

txt = input("Give me a number please: ")

try:
    num = int(txt)
    print("The number you gave is ", num)
except ValueError:
    print("Please put in a real number, not a string or text")
