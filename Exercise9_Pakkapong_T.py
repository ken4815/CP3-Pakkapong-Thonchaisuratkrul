username = input("Username :")
password = input("Password :")
LoginLeft = 2
while username != "Pakkapong" or password != "5252" :
    print("Try again")
    username = input("Username :")
    password = input("Password :")
    LoginLeft = LoginLeft - 1
    if LoginLeft == 0 :
        print("Try again next time")
        break
if username == "Pakkapong" and password == "5252" :
    print("done!")
