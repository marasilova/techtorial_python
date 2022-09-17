fruits=("strawberry","apple","orange","banana","orange")

print(fruits)
print(type(fruits))

print(fruits.index("apple"))  #->1
print(fruits.count("orange")) #->2

# Accessing the elements of a tuple
# we can use index numbers as we did with list.
#getting the third element from tuple
print(fruits[2])

#Using for loop with tuples.

for element in fruits:
    print(element)

# Create a loop 
#fruits=("strawberry","apple","orange","banana","orange")

#From this tuple print out first fruits name 
#that has odd length. If there is no fruit with odd 
#lenght print odd length couldn't be found.


odd_fruit = ""
for fruit in fruits:
    if len(fruit)%2!=0:
        # I have found odd length
        odd_fruit = fruit
        break

if odd_fruit!="":
    print("First odd fruit is",odd_fruit)
else:
    print("Odd length fruit is not found.")
