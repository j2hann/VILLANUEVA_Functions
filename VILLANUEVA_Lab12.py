# List of food items and their prices 
foodItems = [
    ("Burger", 30),
    ("Cheeseburger", 40),
    ("Hotdog", 25),
    ("Footlong", 45),
    ("Fries", 50)
]

# List to store the customer's order
order = []
x = 1

# Function to calculate the total cost of ordered items
def calculateTotal(order):
    totalCost = 0
    for item in order:  
        for food, price in foodItems:
            if food == item:
                totalCost += price
                break
    return totalCost

# Print welcome message and menu
print("Welcome to the Angel's Burgers!")
print()
print("Menu: ")
for item, price in foodItems:
    print(item + ": PHP" + str(price))
print()

# Order input loop
while True:
    orderItem = input("Enter the food item you want to order (Type 'end' to finish): ").capitalize()
    
    if orderItem == "End":
        break
    else:
        if any(item == orderItem for item, price in foodItems):
            order.append(orderItem)
        else:
            print("Invalid item. Please select from the menu.")

# If the user has already entered something, show the order and calculate how much it costs all together
if order:
    print()
    print("Your order:")
    for item in order:
        print(str(x) + ". " + item)
        x += 1
    print()
    
    # Calculate amount using the function above
    totalCost = calculateTotal(order)
    print("Total amount: PHP" + str(totalCost))
    
    # Payment loop
    while True:
        payment = float(input("Enter your payment: PHP"))
        
        if payment < totalCost:
            print("Insufficient payment. Please enter a valid amount.")
        else:
            change = payment - totalCost
            print()
            print("Payment successful! Your change is: PHP" + str(round(change, 2)))
            break
else:
    print("No items ordered. Thank you for visiting!")