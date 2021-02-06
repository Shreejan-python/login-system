users = {}
status = ""
 
def displayMenu():
    status = input("Are you registered user? y/n? Press q to quit: ")
    if status == "y":
        oldUser()
    elif status == "n":
        newUser()
 
def newUser():
    createLogin = input("Create login name: ")
 
    if createLogin in users:
        print("Login name already exist!\n")
    else:
        password = input("Create password: ")
        users[createLogin] = password
        print("\nUser created\n")
 
def oldUser():
    login = input("Enter login name: ")
    passw_ = input("Enter password: ")
 
    if login in users and users[login] == passw_:
        print("\nLogin successful!\n")
    else:
        print("\nUser doesn't exist or wrong password!\n")
 
while status != "q":
    displayMenu()