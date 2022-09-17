#User wants to deposit his money intio his bank account
#He already has $200 in his account
#He has 3 different paychecks which are (400,600,350)
#He can only deposit one paycheck at a time
#After he deposit all the money in the account
#He bought a phone for $599, and headphone for $299
#Create a python programm to calculate his final money in the account.
#Use input function to get all values


bank_account=200

spent1=599
spent2=299

print("You can deposit first paycheck amount you want to deposit")
first_deposit=int(input())
bank_account+=first_deposit

print("You can deposit second paycheck amount you want to deposit")
second_deposit=int(input())
bank_account+=second_deposit

print("You can deposit third paycheck amount you want to deposit")
third_deposit=int(input())
bank_account+=third_deposit

print("Please enter the dollar amount of phone you want to buy")
phone=int(input())
bank_account-=phone
print("Please enter the dollar amount of headphone you want to buy")
headphone=int(input())
bank_account-=headphone
print("His final money in the bank account is", bank_account)