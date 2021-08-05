menu_list = [
    {"id": 1, "name": "1. Sweet and Sour Spare Ribs", "price": 34, "$": "yuan"},
    {"id": 2, "name": "2. Sweet and Sour Fish", "price": 23, "$": "yuan"},
    {"id": 3, "name": "3. Big Chicken", "price": 65, "$": "yuan"},
    {"id": 4, "name": "4. Braised Pork", "price": 66, "$": "yuan"},
    {"id": 5, "name": "5. Pork dumplings", "price": 21, "$": "yuan"}]
Order_list = []
print(
    '========================== Welcome to Wanglaogou Restaurant, I wish you a happy meal ============ ======================== ')
print("Today's menu: ")
for menu in menu_list:
    print(menu.get('name'), menu.get('price'), menu.get('$'))
while True:
    print('=' * 50)
    print("1. User order \ n2. Cancel order \ n3. Confirm menu \ n4. Checkout")
    server = int(input("Please select service:"))
    if server == 1:
        while True:
            menu_add = input("Please enter the dish name number or enter Y to end the order:")
            if menu_add.upper() != 'Y':
                for m in menu_list:
                    if m.get('id') == int(menu_add):
                        Order_list.append(m)
                        break
            else:
                print('================== Ordered =====================')
                total_price = 0
                for order in Order_list:
                    print(order.get('name'), order.get('price'), order.get('$'))
                    total_price += int(order.get('price'))
                print('Subtotal: {} yuan'.format(total_price))
                break
    elif server == 2:
        menu_del = input("Please enter the name of the dish to be cancelled:")
        for order in Order_list:
            if order.get('id') == int(menu_del):
                Order_list.remove(order)

        print('================== Ordered =====================')
        total_price = 0
        for order in Order_list:
            print(order.get('name'), order.get('price'), order.get('$'))
            total_price += int(order.get('price'))
        print('Subtotal: {} yuan'.format(total_price))
    elif server == 3:
        print('================== Ordered =====================')
        total_price = 0
        for order in Order_list:
            print(order.get('name'), order.get('price'), order.get('$'))
            total_price += int(order.get('price'))
        print('Subtotal: {} yuan'.format(total_price))
    elif server == 4:
        print('================= Your consumption menu =======================')
        total_price = 0
        for order in Order_list:
            print(order.get('name'), order.get('price'), order.get('$'))
            total_price += int(order.get('price'))

        print('Total consumption: {} yuan'.format(total_price))

        print('================== Welcome you to visit again, goodbye! =====================')
        break