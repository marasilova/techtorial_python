#Ask user to give you a string filled with cat and dog texts
#From the given string if number of dogs and cats is the same print True

print("Give a string consist of dog and cat words")
str=input()

count_of_dogs=str.count("dog")
print(type(count_of_dogs))

count_of_cats=str.count("cat")

#This method is case sensitive
is_count_same= count_of_dogs == count_of_cats

print(is_count_same)

#Ask user to give two different string values
#If the first string contains the second string
#print True, if not return False

print("Enter some text")
str1=input()

print("Enter some text")
str2=input()

#If the first strin doesn't contain the second string
#count of second string in the first one should be 0

count2=str2.count(str1)
is_contain=bool(count2)

print(is_contain)


