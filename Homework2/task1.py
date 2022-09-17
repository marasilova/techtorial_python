# Please use method chaining for the following Strings. Methods are
# provided next to the String.
# String “ Snicker " —> strip, upper, remove prefix and slice the string with
# any number of your choice
# String “Cookie” —> lower, replace ‘o’ with ‘u’, remove suffix e, 
# starts with ‘C’


word="Snicker"
print(word.strip("r").removeprefix("Sn").upper()[0:2])

word1="Cookie"

print(word1.lower().replace("o","u").removesuffix("e").startswith("C"))
