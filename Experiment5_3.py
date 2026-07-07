# Task 3: Delivery fee calculation
weight = float(input("Enter package weight (in kg): "))

if weight <= 1:
    fee = 10
    print(f"Delivery fee: {fee} RMB")
elif weight <= 3:
    fee = 20
    print(f"Delivery fee: {fee} RMB")
elif weight <= 5:
    fee = 30
    print(f"Delivery fee: {fee} RMB")
else:
    print("Please head to the mail company and we will calculate the delivery fee for you.")
