a="Techtorial"
print(a.upper())

print(a)
#Since the string is immutable,it will not change its value unless
#it is reassigned.

s="PYthon"
print(s.lower())
#Method chaining -> as long as method you use in the string returns
#another string
#you can use other string methods

print(s.lower().upper()) #s will be printed in all upper case 
#since it is the last method
print(s.lower().lower())


a="TechToRial"      #Result of the swapcase is write lower cases as an uppercase,
#uppercases as a lower cases.
print(a.swapcase())

print("Result of the capitalize method", a.capitalize())


