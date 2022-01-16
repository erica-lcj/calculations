# This calculator will tell you in $USD how much each person should pay for a meal, based on how many were dining and what percentage you want to tip.

print("Welcome to the tip calculator.")
bill = float(input("What was your total bill?\n$"))
print("What percentage tip would you like to give? 10%, 12%, or 15%")
tip = int(input())
people = int(input("How many people are splitting the bill?\n"))

split = (bill/people)*((tip/100)+1)
print(f"Each person should pay ${round(split, 3)}.")
