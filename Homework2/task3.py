#Using the input function ask the user to enter one sentence with three
# words and print the index number of each word's last character and then
# print the sum of each index number that you found.

print("Please enter one sentence with three words")
s1=input()
space1=s1.find(" ")
last_of_first=space1-1
space2=s1.rfind(" ")
last_of_second=space2-1
last_of_third=len(s1)-1

total=last_of_first+last_of_second+last_of_third
print(f"The sum {total}")