# CTI 110
# 10/29/2024
# Hughes Jamie
# Module grades

print("Module grades")
mod1 = float(input("Module 1: "))
mod2 = float(input("Module 2: "))
mod3 = float(input("Module 3: "))
mod4 = float(input("Module 4: "))
mod5 = float(input("Module 5: "))
mod6 = float(input("Module 6: "))

module_grades = [mod1, mod2, mod3, mod4, mod5, mod6]
print("RESULTS")
print("Lowest: ", min(module_grades))
print("Highest: ", max(module_grades))
print("Sum of grades: ", sum(module_grades))
average = sum(module_grades) / len(module_grades)
# example: print(format(99.999999, ".2f")
print("Grades' average: ", format(average,".2f"))
