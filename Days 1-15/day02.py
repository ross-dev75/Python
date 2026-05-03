print("Welcome to the tip calculator!")

# get the total bill amount, including change, in a float
bill = float(input("What was the total bill? $"))

# get the total tip amount, including change, in another float
tip = (float(input("What percentage tip would you like to give? 10 12 15 ")))

# get the total amount of people in an integer (since you don't need a decimal point for this)
people = int(input("How many people to split the bill? "))

# calculate the total bill amount with the tip included
# multiply the tip percent by 100.
# next multiply that number (1.xx) to the bill to get the amount you're going to tip.
# lastly, add the amount you're going to tip to the bill amount and save that number in a new var.
bill_with_tip = (bill + (bill * (tip / 100)))

# divide the total bill with tip added by the people splitting the check
per_person_cost = bill_with_tip / people

# round the number each person will pay to the second decimal place (100ths place),
# since the lowest amount of money you can pay is 1/100th of one dollar (or one cent)
contribution_each = round(per_person_cost, 2)

# use an 'f string' to place a number inside a string, and print the total each person owes.
print(f"Each person should pay ${contribution_each}")
