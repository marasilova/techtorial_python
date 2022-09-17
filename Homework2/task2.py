# Ask user to enter any string value using input function.
# Then, remove all the spaces (" ") from the given string. 
# After removing the spaces from the string, 
# if the string's length is odd print True, otherwise print False. 

print("Enter a string")
str=input()
print(len(str.replace(" ",""))%2==1)

