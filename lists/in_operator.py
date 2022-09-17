

#Using in operator we can check specified value is in the list or not
#we can also use in operator for strings as well

list=[1,2,3,4,5]

if 2 in list:
    print("2 is in the list")
if 11 in list:
    print("11 is in the list")  # this line will not work because 
    #11 is not in the list


#not in operator will check if the specified value is not in the 
#iterable object

if 6 not in list:
    print(6, "is not in the list")


# ask user to enter a random digit 
#check if the digit is present in our list or not
#if user enter present element
#print you won a price
#if not print maybe next time

print("ENter a random digit")
digit=int(input())

if digit in list:
    print ("you won a price")
elif digit not in list:
    print("maybe,next time")


#in operator can be used for every iterable object:
# < list string range >