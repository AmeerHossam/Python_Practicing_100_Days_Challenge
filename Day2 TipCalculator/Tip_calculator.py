print("Wekcine to the tip calculator.")
total_bill=float(input("What was the total bill?\n>> $"))
percentage_tip=int(input("What percentage tip would you like to give? 10, 12 or 15\n>> %"))/100
people_count=int(input("How many people to split the bill?\n>> "))
calculate_tip=(total_bill*percentage_tip) / (people_count)
print(f"Each person should pay {round(calculate_tip,2)}$")