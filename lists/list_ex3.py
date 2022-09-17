list=[1,5,6,11,90,3,6]

#Print all the odd numbers from index number 3 to 6 inclusive

#I need an index number that is ranging from 3 to 6 inclusive

range(3,7) #->3,4,5

for index in range(3,7):
    if list[index] % 2 !=0:
        print(list[index])


