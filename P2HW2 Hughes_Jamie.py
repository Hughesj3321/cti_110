# CTI 110
# 10/29/2024
# Hughes Jamie
# Module grades

print("Module grades")
mod1 = int(input("Module 1: "))
mod2 = int(input("Module 2: "))
mod3 = int(input("Module 3: "))
mod4 = int(input("Module 4: "))
mod5 = int(input("Module 5: "))
mod6 = int(input("Module 6: "))

module_grades = [mod1, mod2, mod3, mod4, mod5, mod6]
print("RESULTS")
print("Lowest: ", min(module_grades))
print("Highest: ", max(module_grades))
print("Sum of grades: ", sum(module_grades))
average = sum(module_grades) / len(module_grades)
print("Grades' average: ", average)
