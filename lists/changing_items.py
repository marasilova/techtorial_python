

list=["str","str1",False,5]

#I want to change first element of the string with 3
list[0]=3
print(list)  #[3,'str',False, 5]
#List is mutable object.

#changing range of elements
print(list[1:3]) #str1 and False
#I want to change the range of the elements
#from 1 to 3 with "new" and "new1"

list[1:3]=["new","new1"]
print(list) #[3,'new','new1',5]

list=["str","str1",False,5]
list[1:3]=["new","new1","new2","new3","new4"]
print(list) #['str', 'new', 'new1', 'new2', 'new3', 'new4', 5]
