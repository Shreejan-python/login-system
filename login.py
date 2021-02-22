users = []
passwords = []
status = ""
 
def displayMenu():
    status = input("Do you want to register or login? Press q to quit: ")
    if status == "login" or status=='Login':
        oldUser()
    elif status == "Register" or status=='register':
        newUser()
 
def newUser():
    Login_name = input("Create login name: ")
 
    if Login_name in users:
        print("Login name already exist!\n")
    else:
        password = input("Create password: ")
        users.append(Login_name)
        print(users)
        passwords.append(password)
 
def oldUser():
    login = input("Enter login name: ")
    
 
    if login in users:
        print(f"\nUsername {login} exists, so you need to enter your password\n")
        passw_ = input("Enter password: ")
        if passw_ in passwords:
            print("\n Successfully login\n")
    else:
        print("\nUser doesn't exists\n")
 
while status != "q":
    displayMenu()