

# Ask the user to enter one number between 1 to 10 then, Write the
# program to print the string in the following format:
# Search to see what happens when you multiply the string with
# numbers and use it for solving this question



print("Please enter a number between 1 to 10")
num=int(input())

duplicated=""
numbers=1
for n in range(0,num):
    duplicated+=str(numbers)
    duplicated=str(numbers)*numbers
    numbers+=1
    print(duplicated)

    





   

    
