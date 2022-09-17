num1,num2=4,6
print(num1==num2) #False

is_num_equal= num1==num2

print(is_num_equal) #False
print(type(is_num_equal)) #bool

print(is_num_equal==(num1==num2)) #True
print(num1!=4)  #False because value of the variable num1 is 4

comparison= num1!=num2 
print(comparison) #True

b3=num1>num2
print(b3)  #False

num1+=2
# On the line above num1 will take the value 6 and since 6 is bigger equals to num2 
# the following line will out put True
print(num1>=num2) #True
