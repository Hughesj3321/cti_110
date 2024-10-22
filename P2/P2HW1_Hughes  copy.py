# CTI 110
# P2HW1
# J Hughes
# 10/10/24

# This program is a enhanced travel budget

print("✈️  Trip calculator ✈️")
print()
# Ask user to enter their budget
budget = float(input("What is your travel budget? $"))
# Where are they going?
destination = input("Where are you going?")
# Gas money?
gas =float(input("How much do you plan to spend on gas? $"))
# Hotel money?
hotel = float(input("What are you planing to spend on a hotel? $"))
# Food money?
food = float(input("What is your food allowance? $"))
# TOTAL
expenses = gas+hotel+food
tax = .08*expenses
print("tax: \t$", format(tax, ".2f"))
total = expenses+tax
print("total: $", format(total,".2f"))
# Remaining amount
Remaining_balance = budget-total
print("Remaining balance: $", format(Remaining_balance, ".2f"))