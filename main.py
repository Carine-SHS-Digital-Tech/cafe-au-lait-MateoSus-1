Cappuccino = float(3.00)
Expresso = float(2.25)
Latte = float(2.50)
IcedCoffee = float(2.50)

Drinks_List = []
Price_List = []
Quantity_List = []

GST = Price_List*int(1.1)
Surcharge = GST*int(1.05)

Order_Method = input("'N' for New Order,\n'T' for Take Away;\nOrder Method: ")
if Order_Method == "N" or "n":
    price = Surcharge
    print("New Order")
elif Order_Method == "T" or "t":
    price = GST
    print("Take-Away")

