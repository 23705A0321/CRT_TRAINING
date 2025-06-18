product_prices = {
    'apple': 50,
    'banana': 30,
    'milk': 20,
    'bread': 50,
    'eggs': 7,
    'rice': 100,
    'chicken': 250
}
customer_cart = {}
total = 0.0
print("Welcome to the Grocery Store!")
print("Available items:", ', '.join(product_prices.keys()))
print("Type 'done' to finish.\n")
while True:
    item = input("Enter item to add: ").strip().lower()
    if item == 'done':
        break
    if item not in product_prices:
        print("Item not found. Please try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity of {item}: "))
        if quantity <= 0:
            print("Quantity should be positive.")
            continue
    except ValueError:
        print("Invalid quantity. Please enter a number.")
        continue
    customer_cart[item] = customer_cart.get(item, 0) + quantity
    item_total = product_prices[item] * quantity
    total += item_total
    print(f"Added {quantity} x {item} (RS{product_prices[item]:.2f} each) = RS{item_total:.2f}")
    print(f"Running Total: RS{total:.2f}\n")
print("\n----- FINAL BILL -----")
for item, quantity in customer_cart.items():
    item_total = product_prices[item] * quantity
    print(f"{item.title()}: {quantity} x RS{product_prices[item]:.2f} = RS{item_total:.2f}")
print("----------------------")
print(f"Total: RS{total:.2f}")

