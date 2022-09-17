

print("Enter a string")
str = input()
str=str.replace(" ","")
new=""
# we should check for each letter, if there is duplication
index =0
while index<len(str):
    if str.count(str[index])>1:
        # it means there is duplicated letter
        
        new=str[index]
        print(str.replace(new,""))
    index+=1

 
