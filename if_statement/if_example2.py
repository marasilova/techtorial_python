#Ask user to enter a positive integer number
#check if the given number is wihtin 2 of a multiple 10
#If it is within 2 of a multiple 10 print
#Your number is within 2 of a multiple 10 
#If not print your number didn't match the expected requirment

#10 -20 -30 -40 -50 

#If user gives 21 ->Your number is within 2 of a multiple 10 
#              43 ->Your number is within a multiple 10
#              39 ->Your number is within 2 of a multiple 10 
#We need to use remainder operator

#If the given number remainder with 10 is less than equals to 2
#It means it is within 22 of a multiple 10
#11%10 ->1
#22%10 ->2
#30%10 ->0

#If the given number remainder with 10 is bigger or equal to 8
#The given number is within 2 of a multiple
print("Please enter a positive integer number")
number=int(input())
remainder=number%10


if remainder>=8 or remainder<=2:
    print("Your number is within 2 of a multiple 10")
else:
    print("your number didn't match the expected requirment")
