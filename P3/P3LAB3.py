# CTI 110
# 10/29/2024
# Hughes Jamie
# Module grades
# P3LAB3
# Convert a numbe grade(0-100)
# to a letter grade

num_grade = int(input("What is the grade (0-100):"))
letter_grade = "" #placeholder

# ten point scale
if num_grade >= 90:
    letter_grade = "A"
elif num_grade >= 80:
    letter_grade = "B"
elif num_grade >= 70:
    letter_grade = "C"
elif num_grade >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

print("Your letter grade is:", letter_grade)

