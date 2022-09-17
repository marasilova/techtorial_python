str1="Welcome to the Techtorial Devops Bootcamp"
str2="amp means in physics unit of measure of the rate of electron flow"

last_three_letters=str1[len(str1)-3] + str1[len(str1)-2] + str1[len(str1)-1] 
print(last_three_letters)

first_three_letters=str2[0] + str2[+1] + str2[+2]

print(first_three_letters)

same_or_not= last_three_letters == first_three_letters
print("Last 3 letters of the string1 is the same with first letters of the string2",same_or_not)