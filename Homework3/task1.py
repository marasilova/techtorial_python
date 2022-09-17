

# Reverse a given String and print it, if they have space in the
# beginning and at the end then remove it.  Without using
# slicing [ : :-1]. Try doing with for loop or while loop


### OLD VERSION ###

# str=” Hello ”
# str=str.replace(” “,”“)
# length=len(str)
# index=1
# while index<=length:
#     print(str[-index])
#     index+=1



### NEW VERSION: GOOGLE HELPED ###
str=" Happy "
str=str.replace(" ","")

reverse=""
length=len(str)

while length>0:
    reverse+=str[length-1]
    length=length-1

print(reverse)



