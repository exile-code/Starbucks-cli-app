username = input("Create a Username :")
Password = input("Create a Password :")
print("Account Created.")

for i in range(3):
    username_input = input("Enter Username : ")
    from getpass import getpass
    password_input = getpass("Enter Password :")
    
    if username_input == username and password_input == Password:
        print("You are logged in.")
        break
    elif username_input != username:
        print("Wrong Username.")
    else:
        print("Wrong Password.")
else:
    print("Access Denied.")