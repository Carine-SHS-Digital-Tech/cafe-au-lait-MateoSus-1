Cappuccino = float(3.00)
Expresso = float(2.25)
Latte = float(2.50)
IcedCoffee = float(2.50)

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
if Order_Method == "D":
    price = Surcharge
    print(D)
elif Order_Method == "d":
    price = Surcharge
    print(d)
elif Order_Method == "T":
    price = GST
    print(T)
elif Order_Method == "t":
    price = GST
    print(t)
else:
    print("Unknown command, please try again")
