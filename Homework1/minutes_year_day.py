minutes=3456789

min=60
hour=24
day=365
year=day*hour*min     #total minutes in a year

total_year=minutes//year
#print(total_year)
after=minutes%year

even_after_days=after//(min*hour)
#print(even_after_days)

print(minutes,"is approximately", total_year, "years and", even_after_days,"days")