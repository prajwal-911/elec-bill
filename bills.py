units = float(input("Enter the number of units consumed: "))

rate = 5  

bill = units * rate

discount = bill * 0.10
discounted_bill = bill - discount

print(f"Electricity Bill = ₹{bill:.2f}")
print(f"Discount (10%) = ₹{discount:.2f}")
print(f"Amount Payable = ₹{discounted_bill:.2f}")
