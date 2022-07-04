# Denise Teo
# 214329G
DrinkDict = {'IM': {'description': 'Iced Milo', 'price': 1.5, 'quantity': 2},
             'HM': {'description': 'Hot Milo', 'price': 1.2, 'quantity': 30},
             'IC': {'description': 'Iced Coffee', 'price': 1.5, 'quantity': 30},
             'HC': {'description': 'Hot Coffee', 'price': 1.2, 'quantity': 30},
             '1P': {'description': '100 Plus', 'price': 1.1, 'quantity': 30},
             'CC': {'description': 'Coca Cola', 'price': 1.3, 'quantity': 0}}


def add_drink_type(drink_id, description, price, quantity):
    new_drink = {drink_id.upper(): {'description': description.title(), 'price': price, 'quantity': quantity}}
    DrinkDict.update(new_drink)
    print("{} has been added".format(DrinkDict[drink_id.upper()]['description']))


def replenish_drink(drink_id, quantity):
    DrinkDict[drink_id.upper()]['quantity'] += quantity


def purchased_drink():
    for i in drink_purchase:
        DrinkDict[i]['quantity'] -= 1


while True:
    display = input("Are you a vendor (Y/N) ? ")
    DrinkMenu = ["IM. Iced Milo (S$1.50)", "HM. Hot Milo (S$1.20)", "IC. Iced Coffee (S$1.50)",
                 "HC. Hot Coffee (S1.20)", "1P. 100 Plus (S$1.10)", "CC. Coca Cola (S$1.30)", "0. Exit / Payment"]
    VendorMenu = ["1. Add Drink Type", "2. Replenish Drink", "0. Exit"]

    if display == 'Y' or display == 'y':
        print("Welcome to ABC Vending Machine. \n")

        Transaction = True
        while Transaction:
            for x in DrinkDict:
                if DrinkDict[x]['quantity'] == 0:
                    print("{:2s}. {:20s}(S${:.2f})  ***Out Of Stock***".format(x, DrinkDict[x]['description'], DrinkDict[x]['price']))
                else:
                    print("{:2s}. {:20s}(S${:.2f})   Qty: {}".format(x, DrinkDict[x]['description'], DrinkDict[x]['price'], DrinkDict[x]['quantity']))
            print("\nSelect from the following choices to continue: ", *VendorMenu, sep="\n")
            choice = input("Enter Choice: ")
            if choice == '1':
                price = 0
                quantity = 0
                while True:
                    drink_id = input("Enter drink id: ")
                    if drink_id.upper() != '' and drink_id.upper() in DrinkDict:
                        print("Drink id exist!")
                        continue
                    elif drink_id.upper() != '' and drink_id.upper() not in DrinkDict:
                        while True:
                            description = input("Enter Description: ")
                            if description == '':
                                print("Empty description, enter again")
                                continue
                            else:
                                break
                        while True:
                            price = input("Enter price: $")
                            if price != '' and price.isalpha():
                                print("Please enter a valid value")
                                continue
                            elif price != '':
                                price = float(price)
                                if price > 0:
                                    break
                                else:
                                    print("Please enter a valid value")
                                    continue
                            else:
                                print("Please enter a valid value")
                                continue
                        while True:
                            quantity = input("Enter quantity: ")
                            if quantity != '' and quantity.isnumeric():
                                quantity = int(quantity)
                                break
                            else:
                                print("Please enter a valid quantity")

                        add_drink_type(drink_id, description, price, quantity)
                    else:
                        print("Error! Please enter a drink id")
                        continue
                    break

            elif choice == '2':
                for x in DrinkDict:
                    if DrinkDict[x]['quantity'] == 0:
                        print("{:2s}. {:20s}(S${:.2f})  ***Out Of Stock***".format(x, DrinkDict[x]['description'], DrinkDict[x]['price']))

                    else:
                        print("{:2s}. {:20s}(S${:.2f})   Qty: {}".format(x, DrinkDict[x]['description'], DrinkDict[x]['price'], DrinkDict[x]['quantity']))

                replenish = True
                while replenish:
                    drink_id = input("Enter drink id: ")
                    if drink_id.upper() in DrinkDict:
                        if DrinkDict[drink_id.upper()]['quantity'] > 5:
                            print("No need to replenish. Quantity is greater than 5.")
                            replenish = False
                            break
                        elif DrinkDict[drink_id.upper()]['quantity'] < 5:
                            while True:
                                quantity = input("Enter quantity: ")
                                if quantity != '' and quantity.isnumeric():
                                    quantity = int(quantity)
                                    if quantity > 0:
                                        replenish_drink(drink_id, quantity)
                                        print("{} has been top up!".format(DrinkDict[drink_id.upper()]['description']))
                                        replenish = False
                                        break
                                    else:
                                        print("Please enter a quantity more than 0.")
                                else:
                                    print("Please enter a valid quantity!")
                    else:
                        print("No drink with this drink id. Try again.")
            elif choice == '0':
                Transaction = False
                break
            else:
                print("Invalid option")

    elif display == 'N' or display == 'n':
        print("Welcome to ABC Vending Machine. \nSelect from the following choices to continue: ")
        for x in DrinkDict:
            if DrinkDict[x]['quantity'] == 0:
                print("{:2s}. {:20s}(S${:.2f})  ***Out Of Stock***".format(x, DrinkDict[x]['description'], DrinkDict[x]['price']))
            else:
                print("{:2s}. {:20s}(S${:.2f})   Qty:{}".format(x, DrinkDict[x]['description'], DrinkDict[x]['price'], DrinkDict[x]['quantity']))
        print("0. Exit / Payment")
        purchasing = True
        qty = 0
        total = 0
        price = 0
        quantity = ""
        drink_purchase = []
        while purchasing:
            choice = input("Enter Choice: ")
            if choice.upper() in DrinkDict:
                if DrinkDict[choice.upper()]['quantity'] == 0:
                    print("{} is out of stock".format(DrinkDict[choice.upper()]['description']))
                else:
                    price = DrinkDict[choice.upper()]['price']
                    total += price
                    qty += 1
                    print("No. of drinks selected = ", qty)
                    drink_purchase.append(choice.upper())
            elif choice == '0':
                if total > 0:
                    print("Please pay: $%.2f" % total)
                    print("Indicate your payment: ")
                    five = True
                    two = True
                    ten = True
                    while ten:
                        NoOf10 = input("Enter no. of $10 notes: ")
                        five = True
                        two = True
                        if NoOf10.isdigit():
                            NoOf10 = int(NoOf10)
                            TotalAmtOf10 = NoOf10*10
                            if TotalAmtOf10 >= total:
                                change = TotalAmtOf10 - total
                                purchased_drink()
                                print("Thank you! Please collect your change: $%.2f" % change)
                                print("Exiting Vending Machine")
                                purchasing = False
                                break
                            else:
                                while five:
                                    NoOf5 = input("Enter no. of $5 notes: ")
                                    if NoOf5.isdigit():
                                        NoOf5 = int(NoOf5)
                                        TotalAmtOf5 = NoOf5*5
                                        check = TotalAmtOf5 + TotalAmtOf10
                                        if check >= total:
                                            change = check - total
                                            purchased_drink()
                                            print("Thank you! Please collect your change: $%.2f" % change)
                                            print("Exiting Vending Machine")
                                            purchasing = False
                                            five = False
                                            ten = False
                                            break
                                        else:
                                            while two:
                                                NoOf2 = input("Enter no. of $2 notes: ")
                                                if NoOf2.isdigit():
                                                    NoOf2 = int(NoOf2)
                                                    TotalAmtOf2 = NoOf2*2
                                                    check1 = check + TotalAmtOf2
                                                    if check1 >= total:
                                                        change = check1 - total
                                                        purchased_drink()
                                                        print("Thank you! Please collect your change: $%.2f" % change)
                                                        print("Exiting Vending Machine")
                                                        ten = False
                                                        five = False
                                                        two = False
                                                        purchasing = False
                                                        break
                                                    else:
                                                        if check1 != 0:
                                                            print("Not enough to pay for the drinks")
                                                            print("Take back your cash!")
                                                            ans = input("Do you want to cancel the purchase? Y/N: ")
                                                            if ans.upper() == 'N':
                                                                two = False
                                                                five = False
                                                            elif ans.upper() == 'Y':
                                                                print("Purchase is cancelled. Thank You.")
                                                                purchasing = False
                                                                two = False
                                                                five = False
                                                                ten = False
                                                                break
                                                            else:
                                                                print("Error")
                                                                break
                                                        else:
                                                            print("Not enough to pay for the drinks")
                                                            ans = input("Do you want to cancel the purchase? Y/N: ")
                                                            if ans.upper() == 'N':
                                                                two = False
                                                                five = False

                                                            elif ans.upper() == 'Y':
                                                                print("Purchase is cancelled. Thank You.")
                                                                purchasing = False
                                                                two = False
                                                                five = False
                                                                ten = False
                                                                break
                                                            else:
                                                                print("Error")
                                                                break
                                                else:
                                                    print("Invalid Amount!")
                                    else:
                                        print("Invalid Amount!")
                        else:
                            print("Invalid Amount!")
                else:
                    print("Exiting the Vending Machine! Good Bye!")
                    purchasing = False
                    break
            else:
                print("Invalid Choice")
    else:
        print("Invalid Option. Exiting Vending Machine")
