Cappuccino = float(3.00)
Espresso = float(2.25)
Latte = float(2.50)
IcedCoffee = float(2.50)

Order_Type = []
Drinks_List = []
Price_List = []
Quantity_List = []

GST = Price_List*int(1.1)
Surcharge = GST*int(1.05)

D = "Dine-In"
d = "Dine-In"
T = "Take-Away"
t = "Take-Away"

Order_Method = input("[D] for Dine-In\n[T] for Take-Away\nOrder Method: ")
if Order_Method.upper() == "D":
    price = Surcharge
    print(D)
elif Order_Method.upper() == "T":
    price = GST
    print(T)
else:
    print("Unknown command, please try again")

menu = input("\nWhat would you like to order from our menu today? (1-4):"
             "\n•(1) Cappuccino    [$3.00]\n•(2) Espresso      [$2.25]"
             "\n•(3) Latte         [$2.50]\n•(4) Iced Coffee   [$2.50]\n")

Cappuccino = 1
Espresso = 2
Latte = 3
IcedCoffee = 4

count = 0
if menu == "1":
    count = count + 1
    Quantity = input(f"How many {1.}'s would you like? ")
    print(f"Cappuccino * {Quantity}")
    while count < 4:
        Order_Again = input("\nWould you like anything else? (Y/N): ")
        if Order_Again.upper() == "Y":
            input("What else would you like to order? (1-4): ")

elif menu == "2":
    count = count + 1
    Quantity = input("How many Espresso's would you like? ")
    print(f"Espresso * {Quantity}")
    Order_Again = input("\nWould you like anything else? (Y/N): ")
    if Order_Again.upper() == "Y":
        input("What else would you like to order? (1-4): ")

elif menu == "3":
    count = count + 1
    Quantity = input("How many Latte's would you like? ")
    print(f"Latte * {Quantity}")
    Order_Again = input("\nWould you like anything else? (Y/N): ")
    if Order_Again.upper() == "Y":
        input("What else would you like to order? (1-4): ")

elif menu == "4":
    count = count + 1
    Quantity = input("How many Iced Coffee's would you like? ")
    print(f"Iced Coffee * {Quantity}")
    Order_Again = input("\nWould you like anything else? (Y/N): ")
    if Order_Again.upper() == "Y":
        input("What else would you like to order? (1-4): ")



#Drinks_List.append(menu)
#print(Drinks_List)