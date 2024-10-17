# CTI 110
# P2LAB2
# Hughes
# 10/17/24

# Example list
numbers = [1, 2, 3, 4]
print(numbers)

# ask the user to enter four numbers
print("Please enter four numbers (enter after each)")
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

my_numbers = [num1, num2, num3, num4]
print("You entered these numbers:", my_numbers)
print("There are", len(my_numbers), "numbers.")
print("Smallest: ", min(my_numbers))
print("Largest: ", max(my_numbers))
print("The total is: ", sum(my_numbers))
# average is total divided by number of items
# len = count of items
average = sum(my_numbers) / len(my_numbers)
print("The average: ", average)

# part 2 - turtle graphics
# basic for loop
for number in my_numbers:
    print(number)

# next, draw using for loops

