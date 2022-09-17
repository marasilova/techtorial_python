#Ask user to give you two integer numbers
#Find the sum of these two integer numbers
#If the sum of these two integer is smaller then 10
#print sum of these two numbers is 10
#If sum of these two number is between 10-19 inclusive,
#print sum of these numbers is 20
#for all other conditions
#print the actual sum of these two numbers

print("Please enter two integer numbers")
num1=int(input())
num2=int(input())
sum=num1+num2

if sum <10:
    print("Sum of these two numbers is 10")
elif sum ==10 and sum < 19:
    print("Sum of these numbers is 20")
else:
    print("The sum of these two integer is",sum)