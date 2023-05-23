print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(
    input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_as_percentage = tip_percentage / 100
total_tip = total_bill * tip_as_percentage
total_bill = total_tip + total_bill
total = total_bill / people
final_total = round(total, 2)

print(f"Each person should pay: ${final_total}")
