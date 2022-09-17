amount=5.22
given_amount=amount*100

quarter_amount=int (given_amount//25)
after_quarter=given_amount-(quarter_amount*25)


dime_amount=int(after_quarter//10)
after_dime=after_quarter-(dime_amount*10)


nickel_amount=int (after_dime//5)
after_nickel=after_dime-(nickel_amount*5)


penny_amount=int (after_nickel//1)
after_penny=after_nickel-(penny_amount*1)


print(amount,"will make", quarter_amount,"quarters", dime_amount, "dimes",nickel_amount,"nickels" ,penny_amount,"pennies")

