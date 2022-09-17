#Ask user to enter a string
#Print each letter in a different line


print("Enter a string")
str=input()

index=0
length=len(str)
while index<length:
    print(str[index])
    index+=1