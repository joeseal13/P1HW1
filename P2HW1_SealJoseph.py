# Joseph Seal
# March 15, 2026
# P2HW1
# Program that calculates and displays travel expenses with formatted output

print("This program calculates and displays travel expenses")

budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How much do you think you will spend on gas? "))
hotel = float(input("Approximately, how much will you need for accommodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

remaining_balance = budget - (gas + hotel + food)

print("\n--------------Travel Expenses--------------")

print(f"{'Location:':20}{destination}")
print(f"{'Initial Budget:':20}${budget:,.2f}")
print(f"{'Fuel:':20}${gas:,.2f}")
print(f"{'Accommodation:':20}${hotel:,.2f}")
print(f"{'Food:':20}${food:,.2f}")

print("-------------------------------------------")

print(f"\nRemaining Balance: ${remaining_balance:,.2f}")
