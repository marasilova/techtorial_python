#Ask user to enter a string and print a rotated 2 version
#where the 2 characters mode to the end
#"Hello" -> "lloHe"
#"java"->"vaja"

print("Enter a word")
s=input()
first_two=s[:2]
rest=s[2:]

s=rest+first_two
print(s)

