day = "Saturday"

letter5th= day[4]
print(day[4])
print(type(letter5th))

print(len(day)) #8

#What is the last index number of the day?
last_index= len(day)-1
print ("Last index is",last_index)

day2="Monday"
#If the last two or first two characters of the day and day2 print True

#What will be the index number for the two characters in the string?
#It will always be 0 and 1

#What will be the index numbers for the last two characters in the string?
#length of the string -1 and -2

first_two_day=day[0] + day[1]
first_two_day2=day2[0] + day2[1]

#condition below will check if the first two charaters of the string is same or not
is_first_same=first_two_day==first_two_day2
print(is_first_same)

last_two_day=day[len(day)-1] + day[len(day)-2]
last_two_day2=day2[len(day2)-1] + day2[len(day2)-2]

#condition below will check if the last two characters of the string is same or not
is_last_same=last_two_day==last_two_day2
print(is_last_same)












