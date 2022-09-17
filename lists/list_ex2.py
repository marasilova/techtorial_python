
nums=[1,2,10,11,13,17,21,26]
#From the given list find the sum of all even numbers
#Lets find sum of all the odds seperately
sum_odd=0
sum=0

for number in nums:
    if number % 2 == 0:
        sum+=number
    else:
        sum_odd+=number
    
print("Sum of all the even numbers from list is", sum)
print("Sum of all the odd numbers from list is", sum_odd)




