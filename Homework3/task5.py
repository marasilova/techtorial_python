

# Using the input function ask the user to enter one string value and
# print only unique letters combined as String also without any space in
# the beginning and at the end.

print("Please enter one string")
str=input()
str=str.removeprefix(" ").removesuffix(" ")

new_version=""
index=0

while index<len(str):
    if str.count(str[index])==1:
        new_version=str.count(str[index])
    index+=1
    print(new_version)