#Ask user to enter two number one smaller than the other
#and print sum of all the numbers that are divisible by 2 and 7 
#between the given two number
#For ex:
#2 50
#output 14+28+42 =84



print("enter a number")
num=int(input())

print("enter a number bigger than first one")
num2=int(input())
sum=0
text=""
for n in range(num,num2):
    if n % 7 == 0 and n %2 == 0:
        text = text + str(n) + " + "
        sum+=n

print(text.removesuffix(" + "), "=",sum)











