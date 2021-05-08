menuList = []
priceList = []

def priceBill():
    total = 0
    print("---- FastFood ----")
    for number in range(len(menuList)):
        print(menuList[number],":",priceList[number],"Baht")
        total += int(priceList[number])
    print("Total :",total)

while True:
    menuName = input("Please enter your Menu")
    if(menuName.lower() == "ok"):
        break
    else:
        menuPrice = int(input("Price :"))
        menuList.append(menuName)
        priceList.append(menuPrice)
priceBill()
