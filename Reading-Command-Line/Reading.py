#Reading Command Line Arguments
import sys

print("The name of our file is: ", (sys.argv[0]))
print("Number of arguments: ", len(sys.argv))
print("The actual arguments: ", str(sys.argv))
