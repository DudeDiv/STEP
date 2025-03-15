"""Problem Statement:
Implement a food ordering system using Python dictionaries and lists.

Tasks:
• Store a menu with food items and their prices.
• Allow users to select multiple food items and enter quantities.
• Calculate the total bill amount and display a summary.

Business Insight:
• Helps understand order processing in a restaurant.

Recommended Output Format:
Menu:
1. Burger - $5
2. Pizza - $8
3. Coffee - $3

Enter item number (0 to stop): 1
Enter quantity: 2
Enter item number (0 to stop): 3
Enter quantity: 1

Order Summary:
Burger x 2 - $10
Coffee x 1 - $3
Total Bill: $13


Hint:
• Use a dictionary to store food items and prices.
• Use a loop to take multiple orders until the user exits.
• Calculate the total bill by multiplying quantity × price."""

#Code:

menu = {
    1: {"name": "Burger", "price": 5},
    2: {"name": "Pizza", "price": 8},
    3: {"name": "Coffee", "price": 3}
}

print("Menu:")
for item_number, details in menu.items():
    print(f"{item_number}. {details['name']} - ${details['price']}")

order = []
while True:
    try:
        item_number = int(input("Enter item number (0 to stop): "))
        if item_number == 0:
            break
        if item_number not in menu:
            print("Invalid item number. Please try again.")
            continue
        quantity = int(input("Enter quantity: "))
        if quantity <= 0:
            print("Quantity must be greater than 0. Please try again.")
            continue
        order.append({
            "item": menu[item_number]["name"],
            "quantity": quantity,
            "price": menu[item_number]["price"]
        })
    except ValueError:
        print("Invalid input. Please enter numbers only.")

print("\nOrder Summary:")
total_bill = 0
for item in order:
    item_total = item["quantity"] * item["price"]
    total_bill += item_total
    print(f"{item['item']} x {item['quantity']} - ${item_total}")

print(f"Total Bill: ${total_bill}")
