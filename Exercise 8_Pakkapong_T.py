username = input("Username : ")
password = input("Password :")
if username == "pakkapong" and password == "5252":
    print("-------welcome to Shop--------")
    print("Choose you item list")
    print("1.Spell shop")
    print("2.Weapon shops")
    type = int(input("Choose your item list"))
    if type == 1:
        print("1.healing spell : 85 coins")
        print("2.Mana spell : 95 coins")
        print("3.Rage spell : 100 coins")
        buy1 = int(input("Choose"))
        if buy1 == 1:
            buy1 = 85
            number = int(input("How many?"))
            allprice = buy1*number
        elif buy1 == 2:
            buy1 = 95
            number = int(input("How many?"))
            allprice = buy1*number
        elif buy1 == 3:
            buy1 = 100
            number = int(input("How many?"))
            allprice = buy1*number
    elif type == 2:
        print("1.wooden sword : 150 coins")
        print("2.Iron sword : 200 coins")
        print("3.limited adamantite sword : 5000 coins")
        buy2 = int(input("Choose"))
        if buy2 == 1:
            buy2 = 150
            number = int(input("How many?"))
            allprice = buy2*number
        elif buy2 == 2:
            buy2 = 200
            number = int(input("How many?"))
            allprice = buy2*number
        elif buy2 == 3:
            buy2 = 5000
            number = int(input("How many?"))
            allprice = buy2*number
    print (allprice , "coins")
    print ("-----Thank you------")
else :
    print("please try again")



