# CTI 110
# P2LAB1
# Hughes
# 10/10/24

# This program adds up sales of something.


item = input("What would you like to purchase today?")
amount = int(input("This is how many i need:"))
value = float(input("The cost per item is: $"))
subtotal = value*amount
print("subtotal: $", format(subtotal, ".2f"))
tax = .08*subtotal
print("tax: \t$", format(tax, ".2f"))
total = subtotal+tax
print("total: \t$", format(total, ".2f"))
