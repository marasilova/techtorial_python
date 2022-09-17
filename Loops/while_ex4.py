#Ask user to enter an integer number and
#print out all the divisirs of the given integer number
#6 -> 1,2,3,6


#Pssible divisors of the given number.
#stars from 1 -> ends at the given number
print("Enter an integer number")
number=int(input())

possible_divisor=1
s=""
while possible_divisor<=number:
    #Since we have the possible divisor but we are not sure 
    # if we can divide the number or not
    #How can I understand if possible_divisor is an actual divisor of the number?
    #if number % possible_divisor is 0 it means possible_divisor
    # is an actual of the number
    if number%possible_divisor==0:
        s+=str(possible_divisor)+", "
        # print(f"{possible_divisor} is an a divisor of the number")
    possible_divisor+=1


# I want to print all divisors in one line like following exapmle
# 1,2,3,6 are the divisors of 6
#Remove suffix only removes if the string is endinf with given character
print(s.removesuffix(", "),"are the divisors of the number")

