list = ["Python","C++","C#","Java","Ruby"]

# Remove the C# from the list? 

list.remove("C#")

print(list) #["Python","C++","Java","Ruby"]

#["Python","C++","Java","Ruby"]

# I want to remove the second element from this list.

list.pop(1)
print(list)
#['Python', 'Java', 'Ruby']

# since the -5 is not in the list it will give index error
# list.pop(-5)
# print(list)
#Index out ouf range error
#list.pop(12)

# If you use bigger or lower indexes to get elements from iterable 
#objects you will index out of range error. 
#print(list[20])

