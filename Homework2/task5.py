# Using an input function enter three different ingredients for the product
# on the same line. Then ask the user to enter any int number. Change the
# first letter of the ingredients starting from the entered number


from pickletools import string1


print("Please enter three ingredients with spaces")
ingredient=input()
print("Please inter int number")
number=input()

first_letter=ingredient[0]
ingredient=ingredient.replace(first_letter,number)
# print(ingredient)

number2=str(int(number)+1)
second_letter=ingredient[ingredient.find(" ")+1]
ingredient=ingredient.replace(second_letter,number2)
# print(ingredient)

number3=str(int(number2)+1)
third_letter=ingredient[ingredient.rfind(" ")+1]
ingredient=ingredient.replace(third_letter,number3)
print(ingredient)