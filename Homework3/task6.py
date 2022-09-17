

# Using a input function enter a sentence that is not separated by space and each
# word starts with upper case. Print given String as separated words with spaces

print("Please enter a sentence without space,instead start word with upper case")
sentence=input()

sentence=sentence.replace(str(sentence.capitalize)," ")
print(sentence)