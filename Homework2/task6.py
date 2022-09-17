#Write the program to get the string value from the specified position.
# First, ask the user to enter one String value. Then ask the user to the
# enter starting number and ending number. After that, print the value
# between the given starting and ending numbers. (Note: since the user
# does not know the python, the user starts counting from 1, and the
# ending number will be included)


print("Please enter a string value")
str=input()

print("Please enter the starting number")
start_number=int(input())-1

print("Please enter the ending number")
ending_number=int(input())

print(str[start_number:ending_number])
