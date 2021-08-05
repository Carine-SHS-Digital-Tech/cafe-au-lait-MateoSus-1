menu = ["Cappuccino", "Espresso", "Latte", "Iced Coffee"]
price = [3.00, 2.25, 2.50, 2.50]

Order_Type = []
Drinks_List = []
Price_List = []
Quantity_List = []

GST = Price_List * int(1.1)
Surcharge = GST * int(1.05)

D = "Dine-In"
d = "Dine-In"
T = "Take-Away"
t = "Take-Away"

Order_Method = input("[D] for Dine-In\n[T] for Take-Away\nOrder Method: ")
while Order_Method.upper() not in ["D", "T"]:
    print("Unknown command, please try again\n")
    Order_Method = input("[D] for Dine-In\n[T] for Take-Away\nOrder Method: ")
else:
    if Order_Method.upper() == "D":
        price = Surcharge
        print(D)
    else:
        price = GST
        print(T)

count = 0
while count < 4:
    item = input("\nWhat would you like to order from our menu today? (1-4):"
                 "\n•(1) Cappuccino    [$3.00]\n•(2) Espresso      [$2.25]"
                 "\n•(3) Latte         [$2.50]\n•(4) Iced Coffee   [$2.50]\n")
    while item in ["1", "2", "3", "4"]:
        count = count + 1
        print(f"You have selected a {menu[int(item) - 1]}")
        Quantity = input(f"How many {menu[int(item) - 1]}'s would you like? ")
        print(f"{menu[int(item) - 1]} * {Quantity}")
        Order_Again = input("\nWould you like anything else? (Y/N): ")
        if Order_Again.upper() not in ["Y", "N"]:
            print("Unknown command, please try again")
        else:
            if Order_Again.upper() == "Y":
                item = input("\nWhat would you like to order from our menu today? (1-4):"
                             "\n•(1) Cappuccino    [$3.00]\n•(2) Espresso      [$2.25]"
                             "\n•(3) Latte         [$2.50]\n•(4) Iced Coffee   [$2.50]\n")
                count = count + 1
            else:
                if Order_Again.upper() == "N":
                    break
    if count > 4:
        break

