chances = 0
correct_password= "shambala"
while chances < 3:
    user_input = input("Enter your Password : ")
    if user_input == correct_password:
        print("Aceess Granted.")
        break
    else:
        print("Wrong Password, try again!")
        chances += 1
else:
    print("Access Denied!")