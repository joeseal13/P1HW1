# Joseph Seal
# March 15, 2026
# P2HW2
# Program that stores module grades in a list and calculates statistics

# Pseudocode
# Ask user for six module grades
# Store the grades in a list
# Calculate lowest grade
# Calculate highest grade
# Calculate sum of grades
# Calculate average of grades
# Display the results formatted to two decimal places

# get grades
m1 = float(input("Enter grade for Module 1: "))
m2 = float(input("Enter grade for Module 2: "))
m3 = float(input("Enter grade for Module 3: "))
m4 = float(input("Enter grade for Module 4: "))
m5 = float(input("Enter grade for Module 5: "))
m6 = float(input("Enter grade for Module 6: "))

# store in list
grades = [m1, m2, m3, m4, m5, m6]

# calculations
lowest = min(grades)
highest = max(grades)
total = sum(grades)
average = total / len(grades)

print("------------Results------------")
print(f"Lowest Grade:      {lowest:.1f}")
print(f"Highest Grade:     {highest:.1f}")
print(f"Sum of Grades:     {total:.1f}")
print(f"Average:           {average:.2f}")
print("--------------------------------")
