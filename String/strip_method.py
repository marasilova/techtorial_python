#given a gmail address from user,print only the user's
#mail name
#Forexample example@gmail.com -> example


print("Please enter your gmail")
gmail=input()
gmail_name=gmail.strip("@gmail.com")
print(gmail_name)


#rstrip method which allows us to just
#remove trailing part of the string

print("Please enter your gmail")
gmail1=input()
gmail1_name=gmail1.rstrip("@gmail.com")
print(gmail1_name)

#lstrip method which allows us to just
#remove leading part of the string

#From the given website below,print only domain name .com
web_site="www.techtorial.com"
print(web_site.lstrip("w."))

#In the strinp method we can easily mistaken, so
# we have to make sure and double check which parts itis going to remove
