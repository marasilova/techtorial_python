#Ask user to enter a password
#If password doesn't have any upper or lower case print False,
#otherwise True

#Password should have upper case and lower case
# "password" will be equal to its lower case version
print("Enter your password")
password=input()
is_there_upper=password != password.lower()

#"PASSWORD will be equal to its upper case version
#if the password is not equal to its case version
#it means there is lower case in the string

is_there_lower=password != password.upper()

is_valid_pass= is_there_lower and is_there_upper

print("Your password is valid", is_valid_pass)
 

