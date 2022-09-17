nums=[1,2,3,1,2,3,4,2,2,2]

#Remove all the duplicated elements from the list

#Remove all the number 2's from thhis list
#First i can find count of 2's in the list
#I can apply the remove method count times.

count=0

for number in nums:
    if number==2:
        count+=1

print(count)
#I need to apply the remove method count times
# i need to create a loop that iterates count times

#range the countis 5
range (count) # 0 1 2 3 4

#How many times the loop will get excuted?
#It will get executed count times
for i in range(count):
    nums.remove(2)
print(nums)

nums = [1,2,3,1,2,3,4,2,2,2]


# Remove all the number 2's from this list.

# I can create a copy of this list
newList = nums.copy()

for number in newList:
    if number == 2:
        nums.remove(2)
print(nums)



