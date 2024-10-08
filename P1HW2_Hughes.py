# CTI 110
# P1HW2
# J Hughes
# 10/08/24

# This program is a travel budget
"""
3. Ask user to enter their budget
4. Ask user to enter travel destination
5. Ask user for amount they will spend on gas
6. Ask user for amount they will spend on accommodation
7. Ask user for amount they will spend on food
8. Add expenses
9. Subtract expenses from budget
10. Display results
"""
print("✈️Trip calculator✈️")
print()
# Ask user to enter their budget
budget = float(input("What is your travel budget? $ "))
# Where are they going?
destination = input("Where are you going?")
# Gas money?
gas =float(input("How much do you plan to spend on gas?"))
# Hotel money?
hotel = float(input("What are you planing to spend on a hotel?"))
# Food money?
food = float(input("What is your food allowance?"))
# TOTAL
total = gas+hotel+food
print("expenses: $", format(total,".2f"))