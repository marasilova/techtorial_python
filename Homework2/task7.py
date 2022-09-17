# 1. Ask the user to enter a random word using input function.
# 2. Then ask the user to input the number of letters that word consists of.
# 3. Lastly ask the user for a letter that they want to learn its index. 
# 4. Your code should print True if the user entered a right number of letters in the
# word. Print False if the wrong number is entered.
# 5. Your code should print the index of the entered letter, if the word doesn’t
# contain the letter then the code should print -1.
# 6. Please look at the example output below to understand how your code
# should work.

print("Please enter a random word")
word=input()
print("Enter the number of letters that word consists")
number=int(input())

if number==len(word):
    print(number==len(word))
else:
    print(False)

print("Please enter a letter that you want to find an index")
letter=input()
index=word.find(letter)

if letter in word:
    print(index)
else:
    print("-1")

