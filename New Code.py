import csv
import os

Item_List = []
Quantity_List = []
Price_List = []

Operation = " "
Item = 0
a = 0

TakeAway_Option = " "
DineIn_Option = " "

Cappuccino_Quantity = 0
Espresso_Quantity = 0
Latte_Quantity = 0
IcedCoffee_Quantity = 0

TotalExcluding_GST = float(0)
TotalIncluding_GST = float(0)
Total = float(0)

Cappuccino_Price = float(3.00)
Espresso_Price = float(2.25)
Latte_Price = float(2.50)
IcedCoffee_Price = float(2.50)

TakeAway_Number = 0
DineIn_Number = 0


Grand_Total = float(0)


while Operation != "3":
    Operation = input("\n•(1) New order\n•(2) Daily Summary\n•(3) Exit\nOperation number (1-3): ")
    if Operation == "1":
        while a == 0:
            a = input("\nOrder Type:\n•(1) Dine-In\n•(2) Take-Away\n")
            if a == "1":
                DineIn_Number = DineIn_Number + 1
                DineIn_Option = " "
            elif a == "2":
                TakeAway_Number = TakeAway_Number + 1
                TakeAway_Option = " "
            else:
                print("Unknown command, please try again.")
                a = 0
        while Item != "":
            Item = input("Menu :\n•(1)Cappuccino    [$3.00]\n•(2)Espresso      [$2.25]\n•(3)Latte         [$2.50]\n•"
                         "(4)Iced Coffee   [$2.50]\n'ENTER' to print reciept\nItem choice: ")
            if Item == "1":
                Cappuccino_Quantity = int(input("Cappuccino quantity: "))
                print(f"Cappuccino * {Cappuccino_Quantity}\n")
                Cappuccino_Total = Cappuccino_Quantity * Cappuccino_Price
                Quantity_List.append(Cappuccino_Quantity)
                Price_List.append(Cappuccino_Total)
                Item_List.append("Cappuccino   ")
                Item = " "
            elif Item == "2":
                Espresso_Quantity = int(input("Espresso quantity: "))
                print(f"Espresso * {Espresso_Quantity}\n")
                Espresso_Total = Espresso_Quantity * Espresso_Price
                Quantity_List.append(Espresso_Quantity)
                Price_List.append(Espresso_Total)
                Item_List.append("Espresso     ")
                Item = " "
            elif Item == "3":
                Latte_Quantity = int(input("Latte quantity: "))
                print(f"Latte * {Latte_Quantity}\n")
                Latte_Total = Latte_Quantity * Latte_Price
                Quantity_List.append(Latte_Quantity)
                Price_List.append(Latte_Total)
                Item_List.append("Latte        ")
                Item = " "
            elif Item == "4":
                IcedCoffee_Quantity = int(input("Iced Coffee quantity: "))
                print(f"Iced Coffee * {IcedCoffee_Quantity}\n")
                IcedCoffee_Total = IcedCoffee_Quantity * IcedCoffee_Price
                Quantity_List.append(IcedCoffee_Quantity)
                Price_List.append(IcedCoffee_Total)
                Item_List.append("Iced Coffee  ")
                Item = " "
            elif Item != "":
                print("Unknown command, please try again.")

            else:
                print("\n\n            CAFE AU LAIT             ")
                print("* * * * * * * * * * * * * * * * * * *")
                print("               RECEIPT               ")
                print("* * * * * * * * * * * * * * * * * * *")
                print("DESCRIPTION                     PRICE")
                b = 0
                for c in range(len(Item_List)):
                    print(f"{Item_List[b]} * {str(Quantity_List[b])}              ${str(round(Price_List[b], 2))}0")
                    Total = Total + Price_List[b]
                    b = b + 1
                    GST = float(1.1)
                    Grand_Total = GST + Total
                    TakeAway_Total = float(GST * Total * 1.1)
                print(f"\nTotal Ex. GST                  ${str(Total)}0")
                print(f"Total Inc. GST                 ${str(round(Grand_Total, 2))}0")
                if a == "1":
                    print("Dine-In")
                    print("* * * * * * * * * * * * * * * * * * *\n")
                elif a == "2":
                    Final_Price = print(f"Take-Away Fee                  ${str(round(TakeAway_Total, 2))}")
                    print("* * * * * * * * * * * * * * * * * * *\n")
                    print(f"Amount Due: ${str(round(GST*Total, 2))}0")
                Payment_Method = input("(1)Cash / (2)Card: ")
                Tendered = 0
                if Payment_Method == "1":
                    while Tendered < Grand_Total:
                        Tendered = float(input("Amount Tendered: "))
                        if Tendered < Grand_Total:
                            print(f"Payment remaining: ${round(Grand_Total-Tendered), 2}")
                        elif Tendered >= TakeAway_Total or Grand_Total:
                            Change = Tendered - (TakeAway_Total) or Grand_Total
                            Change = round(Change, 2)
                        else:
                            print("Unknown command, please try again.")
                else:
                    print("Payment made")
                Info = []
                with open('daily_summary.csv', 'a', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow(Info)

    elif Operation == "2":
        os.system("start EXCEL.EXE daily_summary.csv")
    elif Operation == "3":
        break
    else:
        print("Unknown command, please try again.")

header = ["Order_ID", "Type", "Item_1", "QTY_1", "EXGST_1", "ITEM_2", "QTY_2", "EXGST_2", "ITEM_3", "QTY_3",
          "EXGST_3", "ITEM_4", "QTY_4", "EXGST_4", "ORDER_CUPS", "ORDER_GST", "ORDER_TAX", "ORDER_TOTAL"]

items = [f"Order_ID", {Operation}, "Cappuccino", {Cappuccino_Quantity}, ""]

with open('daily_summary.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)