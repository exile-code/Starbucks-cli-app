#Complete Starbucks
import time
import random
from getpass import getpass


print(" --- Welcome to Starbucks ☕️ --- ")
username = input("Create a Username : ")
password = getpass("Create a Password : ")
print("Account Created.")

for i in range(3):
    username_input = input("Enter Username : ")
    password_input = getpass("Enter Password : ")

    if username_input == username and password_input == password:
        print("You are logged in.")
        break
    
    elif username_input != username:
        print("Wrong Username.")
    
    else:
        print("Wrong Password.")
        time.sleep(5)

else:
    print("Access Denied.")

#main interface
print("Hi! Welcome to Starbucks. What can I get for you today?")
print("Americano    Cappuccino  Latte\nMocha    Macchiato   Flat White\nEspresso    Cortado Affogato")

#order math
orders = []

def calculate_price(size, milk):
    price = 3.0
    if size == "tall":
        price += 0.5
    elif size == "grande":
        price += 1.0
    elif size == "venti":
        price += 1.5
    if milk != "regular":
        price += 0.5
    return round(price, 2)

#order taking part
def take_order(username):
    coffee = input("Enter your choice :")

    #milk selection
    milk = "regular"
    sub = input("Any Milk Substitutions? (Yes/No) : ")
    if sub.strip().lower() == "yes":
        milk = input("What kind of Milk? (Soy/ Almond/ Oat/ Coconut) :").strip().lower()
        
        #size selection
    size = input("What size? (Short/ Tall/ Grande/ Venti) :").strip().lower()

        #temp selection
    temp = input("Would you like your Coffee (Hot/ Iced) :")

    #price calculation 
    price = calculate_price(size, milk)
    wait = random.randint(3, 7)

    order = {
        "name" : username,
        "coffee": coffee,
        "milk": milk,
        "size": size,
        "temp": temp,
        "price": price,
        "wait_time": wait
    }
    return order

def generate_receipts():
    for i, order in enumerate(orders):
        order_id = random.randint(10000, 99999)
        filename = f"receipt_{order_id}.txt"
        with open(filename, "w") as f:
            f.write(f"Order Receipt #{order_id}\n")
            f.write(f"Customer: {order['name']}\n")
            f.write(f"Drink: {order['temp']} {order['size']} {order['coffee']} with {order['milk']} milk\n")
            f.write(f"Price: ${order['price']}\n")
            f.write(f"Estimated wait time:  {order['wait_time']} minutes\n")
        print(f"Receipt saved as {filename}")


while True:
    order = take_order(username)
    orders.append(order)

    print(f"\n✅ Order for {username} confirmed! Your {order['temp'].title()} {order['size'].title()} {order['coffee'].title()} with {order['milk'].title()} milk will be ready in {order['wait_time']} minutes.")
    print(f"Total 💸 : ${order['price']}\n")
    
    again = input("Would you like to add another order? (yes/no): ")
    if again.lower() != "yes":
        break

generate_receipts()
print("\nAll orders complete. Have a great day!")