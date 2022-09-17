

# create a python program to give most efficient 
#exchange possible using only

#coins
#quarter=25
#nickel=5
#dime=10
#penny=1

dollar=2.36
dollar_amount=dollar*100

quarter=25
dime=10
nickel=5
penny=1

count_q=int(dollar_amount//quarter)
#print(count_q)
remaining_exchange=dollar_amount % quarter

count_d=int(remaining_exchange//dime)
#print(count_d)
remaining_exchange_dime=remaining_exchange % dime

count_n=int(remaining_exchange_dime//nickel)
#print(count_n)
remaining_exchange_n=remaining_exchange_dime % nickel

count_p=int(remaining_exchange_n//penny)
#print(count_p)
remaining_exchange_p=remaining_exchange_n % penny

print(dollar, "will make", count_q, "quarters", count_d, "dimes", count_n,"nickels", count_p, "pennies")

