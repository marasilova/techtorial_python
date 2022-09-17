#Ask user to give you a string
#Ask user to give order of the number and print that letter from the string

print("Enter a text")
text=input()

print("Enter the order number of the leteer you want to see")
order_number=int(input())

#We can to consider that user doesn't know the index numbers, and the number
#user provided will be 1 bigger than the index number
#"Python"
# 012345 -> index number
# 123456 -> order number which user will think it is true


index_number=order_number-1
print(text[index_number])