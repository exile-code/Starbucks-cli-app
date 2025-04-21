age = int(input("Enter your Age : "))
    
if age < 18:
        print("Access Denied!")
elif age >= 18 and age <= 65:
        print("Welcome!")
elif age >= 66 and age <= 99:
        print("Ok Boomer!")
elif age==100:
    print("New achievement unlocked!")
else:
    print("You are a Vampire!")

