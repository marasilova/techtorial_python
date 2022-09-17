str="Hello"
str1="Hello"
str2="heLlo"

print(str==str1)
# Equal equal sign is case sensitive,so if the value of the two strings
# are different,it will returns false
print(str1==str2)

str2="hello"
print(str2) #hello

#Sincde we reassgin and change value of the str2
#equal comparison btwn str2 and str1 will give the result as True

print(str2==str1)


#Concatenating the Strings
#Concatenating is addinf more string to the existiong string value

str2= str2 + " world"
print(str2)

#WE can use concetenation even when we are creating the variable first time
str3= "hello" + " world"
print(str3)

str4=str+str1
print(str4) #hellohello

