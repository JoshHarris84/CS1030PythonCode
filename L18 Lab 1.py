# L18 Lab 1: Free Shipping Eligibility
# Asks for the order total and tells the shopper whether shipping is free.

order_total = float(input("Enter your order total: $"))

if order_total >= 50:
    print("You qualify for free shipping.")
else:
    print("Shipping fee required.")