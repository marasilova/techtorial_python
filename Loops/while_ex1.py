# Ask user to give you a string
# From the string print index number of all the e's

print("Enter a text")
str=str.lower(input())


#We can access string elements using their indexes.

index=0
# Index number is alwasy smaller than length of the string
#"Example"
#0123456 Index numbers
#   7   Length of the string

length_of_str=len(str)

while index<length_of_str:
    #If I want to access the element with index number str[index]
    if str[index]=="e":
        print(f"Index number of e is {index}")
    index+=1
