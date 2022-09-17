#prefix -> will remove from the beginning of the string
#suffix -> will remove from the end of the string

s= "Hello Python"

#If you want to remove Python from the string you can use
#remove suffix method

print(s.removesuffix("Python"))

print(s.removeprefix("Hello"))

#This method is case sensitive


#from the given website string,
#print onyl the domain name of the website

print("Enter website name")
s=input()
s=s.removeprefix("www.")
s=s.removesuffix(".com")
print(s)


str="hello world"
print(str.removeprefix("el"))   #it will print as it is

str2="Encapsulation is good for data hiding"
print(str2.removesuffix("idin"))  #it will print as it is
print(str2.strip("gni"))          #it will remove ing at the end





