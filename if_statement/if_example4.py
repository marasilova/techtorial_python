#The doctors say you babies can go out in summer if the weather is 
# between 60 and 80 inclusive.If not they say you shouldn't take the baby out. 
# In the winter they say you can go out if the weather is hotter than -20
# Ask user what season they are in also ask user how hot the weather 
# is and print if they can go out with baby or not. 

from tkinter import W


print("Enter in what season you are?")
season=input()
print("What is the degree of the weather today?")
w=int(input())

if season.lower() == "summer":
    #If this line getting executed this line is summer.
    if w<=80 and w>=60:
        print("You can take baby out.")
    else:
        print("You should not baby take the out.")
elif season.lower() =="winter":
    if w>-20:
        print("You can take baby out")
    else:
        print("You should not baby take the out.")
else:
    print("You should not baby take the out")


