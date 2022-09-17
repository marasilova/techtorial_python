# Ask user to enter an integer number 
#and print multiplication table for given number

#If user enters 3
# 3 * 1 =3
# 3 * 2 =6
# 3 * 3 =9
# .......
# 3 * 10=30


print("Enter an integer number")
num=int(input())

# to use the loop i need to find the range
# On which number multiplication table starts -> 1
# On which number multiplication table ends -> 10

mult=1
mult1=10
while mult<=mult1:
    print(f"{num} * {mult} = {num*mult}")
    mult+=1

