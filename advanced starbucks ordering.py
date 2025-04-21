import random

orders = []

def calculate_price(size, milk):
    price = 3.0
    if size == "Tall":
        price += 0.5
    elif size == "Grande":
        price += 1.0
    elif size == "Venti":
        price += 1.5
    if milk.lower() != "regular":
        price += 0.5
    return round(price, 2)

def take_order():
    print("\n--- New Order ---")
    coffee = input("What coffee would you like? ")
    
    # Milk
    milk = "regular"
    sub = input("Any milk substitution? (yes/no): ")
    if sub.lower() == "yes":
        milk = input("What type of milk? (Soy/Almond/Oat/Coconut): ")

    # Size
    size = input("What size? (Short/Tall/Grande/Venti): ")

    # Temp
    temp = input("Hot or Iced? ")

    # Name
    name = input("Customer name: ")

    price = calculate_price(size, milk)
    wait = random.randint(3, 7)

    order = {
        "name": name,
        "coffee": coffee,
        "milk": milk,
        "size": size,
        "temp": temp,
        "price": price,
        "wait_time": wait
    }
    orders.append(order)

    print(f"\nOrder for {name} confirmed! Your {temp} {size} {coffee} with {milk} milk will be ready in {wait} minutes.")
    print(f"Total: ${price}\n")

def generate_receipts():
    for i, order in enumerate(orders):
        order_id = random.randint(10000, 99999)
        filename = f"receipt_{order_id}.txt"
        with open(filename, "w") as f:
            f.write(f"Order Receipt #{order_id}\n")
            f.write(f"Customer: {order['name']}\n")
            f.write(f"Drink: {order['temp']} {order['size']} {order['coffee']} with {order['milk']} milk\n")
            f.write(f"Price: ${order['price']}\n")
            f.write(f"Estimated wait time: {order['wait_time']} minutes\n")
        print(f"Receipt saved as {filename}")

# Main loop
print("Welcome to Python Starbucks ☕️")

while True:
    take_order()
    again = input("Would you like to add another order? (yes/no): ")
    if again.lower() != "yes":
        break

generate_receipts()
print("\nAll orders complete. Have a great day!")
