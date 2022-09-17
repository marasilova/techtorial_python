s="Techtorial"

print(s[4:7])
print(s[4]+s[7])


#Ask user the enter a string which lenght is odd longer than 3
#and print the middle three letters from the string
# "Chicago"
# "seven"

print("Enter a string which lenght is odd longer")
text=input()

#First I have to find middle index
middle_index=len(text)//2
print(text[middle_index-1:middle_index+2])

