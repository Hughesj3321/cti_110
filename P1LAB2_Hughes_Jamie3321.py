# CTI 110
# P1LAB2 - Recipt
# Norris
# 10/1/24

print("P1LAB2")
# For today, let's do a restaurant
# that only sells burgers and fries

#declare our variables
num_burgers = 0
num_fries = 0
burger_cost = 4.99
fry_cost = 0.99

print("Can I take your order?")
# we have to convert their input to an int
num_burgers = int(input("How many burgers?"))

print("You ordered", num_burgers, "burgers")

num_fries = int(input("How many fries?"))
print("Okay, that's", num_fries, "french fries.")

# Add up all the totals
burger_total = num_burgers * burger_cost
fry_total = num_fries * fry_cost
meal_total = burger_total + fry_total

#print the receipt
print("-" * 20)
print(num_burgers, "burger\t$", burger_total)
print(num_fries,"fry\t\t$", fry_total)
print("-" * 20)
print("Total\t\t$", meal_total)
