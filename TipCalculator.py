#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Write your code below this line 👇

print('Welcome to the tip calculator')
bill = (input("What was the total bill? $"))
tip = (input("What percentage tip would you like to give? 10, 12, or 15? "))
after_tip = float(bill)*(int(tip)/100+1)

people = input("How many people to split the bill? ")
res = round(after_tip/int(people), 2)
# res="{:.2f}".format(after_tip/int(people)) //we may round using this method
print(f"Each person should pay: ${res}")
