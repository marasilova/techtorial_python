

#print numbers from 1 to 10 inclusive

from ast import Num


num=1

while num <= 10:
    print(num)
    # I have to update the valur of variable num in the loop so
    #condition will become false eventually.
    num+=1
print(f"Value of the variable num is {num}")  #11
# Print even numbers that are smaller than equal to 10

num1=2
while num1 <=10:
    print(num1)
    num1+=2
print(f"Value of the variable num is {num1}")   #12

#Print even numbers that are smaller equal to 10
#This time variable num is goint to start from 1

num=1

while num<=10:
    if num %2==0:
        print(num)
    num+=1


#From 1 to 20 inclusive print odd number in following format
#"This is an odd number {Value of number}"
#print every even number
#"This is an even number {Value of number}"

num=1

while num<=20:
    #In the while loop I have to decide num is currently even or odd
    if num %2==0:
        print(f"This is an even number {num}")
    elif num %2==1:
        print(f"This is an odd number {num}")
    #I have to update the valur of the number
    num+=1

# EXAMPLE FOR INFINITE LOOP!!!
# num=0

# while num<1:
#     print("in the while loop")
# print("Outside the while after the infinite loop")