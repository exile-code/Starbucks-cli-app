print("Hi! Welcome to Starbucks!")
print("What can I get for you today? ")
print("Americano    Cappuccino  Latte\nMocha    Macchiato   Flat White\nEspresso    Cortado Affogato")

#coffee selection
def coffee_type(type):
    return f"{type}? Great Choice! "

coffee= input("I'll have a..")
print(coffee_type(coffee))

#milk substitution
print("Would you like any Substitutions for Milk?\nYes/No")
sub_milk = input()

milk = "regular" #default milk
if sub_milk.lower() == 'yes':
    print("What type of milk?\nSoy  Almond  Coconut Oat")
    milk =input("I'll have..")
    print(f"Got it. {milk} milk noted.")
else:
    print("No Substitutions? Alright!")

#size
print("What size would you like?\nShort Tall    Grande  Venti")
size = input("I'll have...")
print(f"{size}? Nice!")

#temperature
print("Would you like your Coffee Hot or Iced?")
temp = input("I'll have it...")
print(f"{temp} it is.")

#Name
print("Can I have your name please?")
customer_name = input()

#final call message
print("\n--- Final Order ---")
print(f"Thanks, {customer_name}! Here's your order: ")
print(f"{temp} {size} {coffee} with {milk} milk.")
print("We'll call your name when it's ready. Enjoy!")