bill_cost = float(input("How much was the bill?\n$"))
split_amount = int(input("How many people are splitting the bill?\n"))
tip_multiplier = input("How much would you like to tip?\n a) 10%\n b) 15%\n c) 20%\n")


while tip_multiplier != "a" and tip_multiplier != "b" and tip_multiplier != "c": 
    tip_multiplier = input("Please answer 'a' , 'b' , or 'c': \n a) 10%\n b) 15%\n c) 20%\n")

if tip_multiplier == "a":   #calculate the amount tipped based on user input
    tip_amount = bill_cost * .10

elif tip_multiplier == "b":
    tip_amount = bill_cost * .15

elif tip_multiplier == "c":
    tip_amount = bill_cost * .20

else:
    print("An Error Occurred.") #this shouldn't ever print but just in case something fucks up why not

total_bill = bill_cost + tip_amount
total_bill = round(total_bill, ndigits=2) #round the float to 2 digits (otherwise you'd get numbers like $22.1202031)
tip_amount = round(tip_amount, ndigits=2)

split_share = total_bill / split_amount
split_share = round(split_share, ndigits=2)
split_tip = tip_amount / split_amount
split_tip = round(split_tip, ndigits=2)

print("Number of guests: ", split_amount ,"\nTip per person: $", split_tip,"\nTotal cost per person: $",split_share,"\nTip amount: $", tip_amount,"\n Total bill: $", total_bill)
