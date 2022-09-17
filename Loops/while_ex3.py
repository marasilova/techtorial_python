# You have $40 in your phone account
#after each call you'll be charged $5
#print --> how much call you can make and
#print how much money left in the account after each call

acct,each_call=40,5
call_number=1


while acct>=each_call:
    print(f"{call_number}th is made")
    call_number+=1
    acct=acct-each_call
    print("After the call I have", acct ,"left")


