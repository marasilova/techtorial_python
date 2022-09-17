#Ask user to enter two numbers,first is greater than the second one
#Find out sum of all the numbers btwn given two number
#first number is 7
#second number is 3


print("Enter your first number")
num1=int(input())
print("Enter your second number")
num2=int(input())

#Before we get to the sum let's print all the numbers between given two number
copyOfnum2 = num2
num2 = num2 +  1
sum = 0
while num2 < num1:
  #  print("In the loop",num2)
  sum += num2
  num2 = num2 +1
print(f"Sum of the numbers between {num1} and {copyOfnum2} is {sum}")  
