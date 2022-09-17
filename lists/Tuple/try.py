fruits=("strawberry","apple","orange","banana","orange")

lenght=len(fruits[0])

for i in fruits:
    if lenght%2==1:
        print(i)
        lenght+=1
else:
    print("Odd length fruit is not found")