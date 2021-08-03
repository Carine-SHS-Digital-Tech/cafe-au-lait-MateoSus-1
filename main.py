menu = ["Cappuccino", "Espresso", "Latte", "Iced Coffee"]
price = [3.00, 2.25, 2.50, 2.50]

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
while Order_Method.upper() not in ["D","T"]:
    print("Unknown command, please try again\n")
    Order_Method = input("[D] for Dine-In\n[T] for Take-Away\nOrder Method: ")
else:
    if Order_Method.upper() == "D":
        price = Surcharge
        print(D)
    else:
        price = GST
        print(T)

item = input("\nWhat would you like to order from our menu today? (1-4):"
             "\n•(1) Cappuccino    [$3.00]\n•(2) Espresso      [$2.25]"
             "\n•(3) Latte         [$2.50]\n•(4) Iced Coffee   [$2.50]\n")

count = 0

if item == "1":
    count = count + 1
    Quantity = input("How many would you like? ")
    print(f"Cappuccino * {Quantity}")
    while count < 4:
        Order_Again = input("\nWould you like anything else? (Y/N): ")
        if Order_Again.upper() == "Y":
            input("What else would you like to order? (1-4): ")
            count = count + 1
            input("How many would you like? ")
        else:

elif item == "2":
    count = count + 1
    Quantity = input("How many would you like? ")
    print(f"Espresso * {Quantity}")
    while count < 4:
        Order_Again = input("\nWould you like anything else? (Y/N): ")
        if Order_Again.upper() == "Y":
            input("What else would you like to order? (1-4): ")
            count = count + 1

elif item == "3":
    count = count + 1
    Quantity = input("How many would you like? ")
    print(f"Latte * {Quantity}")
    while count < 4:
        Order_Again = input("\nWould you like anything else? (Y/N): ")
        if Order_Again.upper() == "Y":
            input("What else would you like to order? (1-4): ")
            count = count + 1

elif item == "4":
    count = count + 1
    Quantity = input("How many would you like? ")
    print(f"Iced Coffee * {Quantity}")
    while count < 4:
        Order_Again = input("\nWould you like anything else? (Y/N): ")
        if Order_Again.upper() == "Y":
            input("What else would you like to order? (1-4): ")
            count = count + 1



#Drinks_List.append(menu)
#print(Drinks_List)
