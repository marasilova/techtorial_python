a=97352
fifth_digit=a%10
a=a//10

fourth_digit=a%10
a=a//10

third_digit=a%10
a=a//10

second_digit=a%10
a=a//10

first_digit=a%10
a=a//10

print(fifth_digit,fourth_digit,third_digit,second_digit,first_digit)


a=str(a)
print(a[::-1])