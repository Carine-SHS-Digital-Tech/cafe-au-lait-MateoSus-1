menu = ["Cappuccino", "Espresso", "Latte", "Iced Coffee"]
price = [3.00, 2.25, 2.50, 2.50]

Drinks_List = []
Price_List = []
Quantity_List = []
Order_Type = []

GST = Price_List * int(1.1)
Surcharge = GST * int(1.05)

D = "Dine-In"
d = "Dine-In"
T = "Take-Away"
t = "Take-Away"

Order_Method = input("[D] for Dine-In\n[T] for Take-Away\nOrder Method: ")
Order_Type.append(Order_Method)
while Order_Method.upper() not in ["D", "T"]:
    print("Unknown command, please try again\n")
    Order_Method = input("[D] for Dine-In\n[T] for Take-Away\nOrder Method: ")
else:
    if Order_Method.upper() == "D":
        price = Surcharge
        print(Order_Type)
    else:
        price = GST
        print(Order_Type)

count = 0
NextOrder = True
#while count < 4:

while NextOrder:
    item = input("\nWhat would you like to order from our menu today? :"
                 "\n•(1)Cappuccino    [$3.00]\n•(2)Espresso      [$2.25]"
                 "\n•(3)Latte         [$2.50]\n•(4)Iced Coffee   [$2.50]\n")
    if item.upper == "1":
        CappuccinoQuantity = input("Cappuccino quantity: ")
        print(f"Cappuccino * {CappuccinoQuantity}")
        Drinks_List.append(menu[0])
        Price_List.append(menu[0])
        count = count + 1

    elif item.upper() == "2":
        EspressoQuantity = input("Espresso quantity: ")
        print(f"Espresso * {EspressoQuantity}")
        Drinks_List.append(menu[1])
        Price_List.append(menu[1])
        count = count + 1

    elif item.upper() == "3":
        LatteQuantity = input("Latte quantity: ")
        print(f"Cappuccino * {LatteQuantity}")
        Drinks_List.append(menu[2])
        Price_List.append(menu[2])
        count = count + 1

    elif item.upper() == "4":
        IcedCoffeeQuantity = input("Iced Coffee quantity: ")
        print(f"Iced Coffee * {IcedCoffeeQuantity}")
        Drinks_List.append(menu[3])
        Price_List.append(menu[3])
        count = count + 1

    else:
        print("Not on the menu, Please try again")
        Order_Again = input("\nWould you like anything else? (Y/N): ")
        if Order_Again == "Y":
            NextOrder = True
        else:
            NextOrder = False
        print(Drinks_List)
        print(Price_List)

print(Drinks_List)
print(Price_List)


