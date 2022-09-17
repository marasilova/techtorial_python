number_of_students=36
str="Total number of the students are" , number_of_students
print(str)

str="Total number of the students are {}"
print(str.format(number_of_students))

number_of_teachers=12
#create a string that shows number of teachers and
#number of students

s="The total of teachers is {} and the total number of student is {}"
print(s.format(number_of_teachers,number_of_students))

#Using index numbers for formatting the string.

s="The total of teachers is {1} and the total number of student is {0}"
print(s.format(number_of_students,number_of_teachers))


s=f"Total number of teachers is {number_of_teachers}"
print(s)