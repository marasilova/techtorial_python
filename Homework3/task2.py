

# Using the input function asks the user to input the min and
# max number. Write a python code that will calculate the sum
# of numbers between the range of min and max and those that
# can only be divided by 3 and 11. 
# (min and max numbers are included)


print("Please enter min number")
min_num=int(input())

print("Please enter max number")
max_num=int(input())+1

sum=0
text=""

for n in range(min_num,max_num):
    if n % 3 == 0 and n % 11 == 0:
        text= text + str(n) + " + "
        sum+=n

print(text.removesuffix(" + "),"=", sum)