menu = ["Cappuccino", "Espresso", "Latte", "Iced Coffee"]
price = [3.00, 2.25, 2.50, 2.50]

Operation = 0

a = 0

Cappuccino_Quantity = 0
Espresso_Quantity = 0
Latte_Quantity = 0
IcedCoffee_Quantity = 0

TakeAway_Number = 0
DineInNumber = 0


Drinks_List = []
Price_List = []
Quantity_List = []
Order_Type = []

GST = Price_List * int(1.1)
Surcharge = GST * int(1.05)

while Operation != "3":
    Operation = input("\n•(1) New order\n•(2) Daily Summary\n•(3) Exit\nOperation number (1-3): ")
    if Operation == "1":
        while a == 0:
            a = input("\nOrder Type:\n•(1) Dine-In\n•(2) Take-Away\n")
            if a == "1":
                DineInNumber = 1
                print("Dine-In")
            elif a == "2":
                TakeAway_Number = 1
                print("Take-Away")

            else:
                print("Unknown command, please try again.")

Operation_Type = input("Mode of Operation: ")

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
        print("Dine-In")
    else:
        price = GST
        print("Take-Away")

print("\nMenu :"
      "\n•(1)Cappuccino    [$3.00]\n•(2)Espresso      [$2.25]"
      "\n•(3)Latte         [$2.50]\n•(4)Iced Coffee   [$2.50]\n")

Next_Order = True
while Next_Order:
    if Operation_Type.upper == "New Order":
        item = input("Item number (1-4): ")
        if item == "1":
            Cappuccino_Quantity = input("Cappuccino quantity: ")
            print(f"Cappuccino * {Cappuccino_Quantity}")
            Drinks_List.append(menu[0])
            Price_List.append(menu[0])

        elif item == "2":
            Espresso_Quantity = input("Espresso quantity: ")
            print(f"Espresso * {Espresso_Quantity}\n")
            Drinks_List.append(menu[1])
            Price_List.append(menu[1])

        elif item == "3":
            Latte_Quantity = input("Latte quantity: ")
            print(f"Cappuccino * {Latte_Quantity}")
            Drinks_List.append(menu[2])
            Price_List.append(menu[2])

        elif item == "4":
            IcedCoffee_Quantity = input("Iced Coffee quantity: ")
            print(f"Iced Coffee * {IcedCoffee_Quantity}")
            Drinks_List.append(menu[3])
            Price_List.append(menu[3])

        else:
            print("Not on the menu, Please try again")
    Order_Again = input("\nWould you like anything else? (Y/N): ")
    if Order_Again == "N":
        Next_Order = False

print(Drinks_List)
print(Price_List)

print(Drinks_List)
print(Price_List)
