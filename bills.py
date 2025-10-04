 #Program to calculate electricity bill with discount

# Input: number of units consumed
units = float(input("Enter the number of units consumed: "))

# Rate per unit
rate = 5  # ₹5 per unit

# Calculate total bill
bill = units * rate

# Apply 10% discount if bill exceeds ₹1000
if bill > 1000:
    discount = bill * 0.10
    bill -= discount
    print(f"10% discount applied: ₹{discount:.2f}")

# Display result
print(f"Electricity Bill = ₹{bill:.2f}")