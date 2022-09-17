#Veera wants lose 10 pounds in one month.
#There are multiple conditon to lose the 10 pounds in a months.
#Veera needs to walk 10000 steps daily or run at least 4 miles a day
#addition to those Veera needs to eat less than 1500 cal daily 
#We shoul create a program to calculate if Veera can loose weight or not

walking_steps=12000
running=3.9
daily_calorie=1499

can_loose_weight= (walking_steps>=10000 or running>= 4) and daily_calorie<1500
print("Veera can loose weight", can_loose_weight)