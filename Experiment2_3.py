item1 = float(input("Enter price of item 1: "))
item2 = float(input("Enter price of item 2: "))
item3 = float(input("Enter price of item 3: "))
item4 = float(input("Enter price of item 4: "))
item5 = float(input("Enter price of item 5: "))


subtotal = item1 + item2 + item3 + item4 + item5 #Subtotal

tax_rate = 0.07
sales_tax = subtotal * tax_rate #Calculate sales tax (7%)

final_price = subtotal + sales_tax # Calculate total

#Display results
print("Amount of purchase: $", subtotal)
print("Sales tax (7%): $", sales_tax)
print("Final Price: $", final_price)
