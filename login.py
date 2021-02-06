users = {}
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
        users[createLogin] = password
        print("User created\n")
 
def oldUser():
    login = input("Enter login name: ")
    passw_ = input("Enter password: ")
 
    if login in users and users[login] == passw_:
        print("\nLogin successful!\n")
    else:
        print("\nUser doesn't exist or wrong password!\n")
 
while status != "q":
    displayMenu()