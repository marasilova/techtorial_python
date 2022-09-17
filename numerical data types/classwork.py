a=234
#find the multiplication of digit of the digit a
# number a will always have three digit number
#2*3*4=24

#when we find remainder with 10,
# it will give us last digit of the number

#a%10=will give the last digit of the number
last_digit=a%10
print(last_digit)

#Following line will remove the last digit of variable a

a=a//10 

middle_digit=a%10
a=a//10

first_digit=a%10

multiplication=last_digit*middle_digit*first_digit

print(multiplication)


#integer division will give us only integer part of the division
#21/5 is 4.20 but if I use integer division
#21//5 is 4


# // When I divide the number by 10 it will give remove the last digit

b=34
print(b%10)

c=67
print(c%10)

d=105
print(d%10)

e=1273
print(e%10)



