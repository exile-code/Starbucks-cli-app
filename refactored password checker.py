import time
from getpass import getpass

def create_account():
    username = input("Create a Username : ")
    password = getpass("Create a Password : ")
    return username, password

def login(correct_user, correct_pass):
    for i in range(3):
        u = input("Username: ")
        p = input("Password: ")
        if u == correct_user and p == correct_pass:
            return True
        print("Wrong Credentials.")
        time.sleep(3)
    return False

def run_auth_flow():
    user, pwd = create_account()
    if login(user,pwd):
        print("Access Granted.")
    else:
        print("Access Denied after 3 attempts.")

run_auth_flow()