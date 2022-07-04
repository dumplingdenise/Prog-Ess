# Denise Teo
# 214329G

while True:
    display = input("Are you a vendor (Y/N) ? ")
    DrinkMenu = ["IM. Iced Milo (S$1.50)", "HM. Hot Milo (S$1.20)", "IC. Iced Coffee (S$1.50)",
                 "HC. Hot Coffee (S1.20)", "1P. 100 Plus (S$1.10)", "CC. Coca Cola (S$1.30)", "0. Exit / Payment"]
    VendorMenu = ["1. Add Drink Type", "2. Replenish Drink", "0. Exit"]

    if display == 'Y' or display == 'y':
        print("Welcome to ABC Vending Machine. \nSelect from the following choices to continue: ")
        print(*VendorMenu, sep="\n")
    elif display == 'N' or display == 'n':
        print("Welcome to ABC Vending Machine. \nSelect from the following choices to continue: ")
        print(*DrinkMenu, sep="\n")
        purchasing = True
        qty = 0
        total = 0
        price = 0
        while purchasing:
            choice = input("Enter Choice: ")
            if choice == 'IM' or choice == 'im':
                price = 1.5
                total += price
                qty += 1
                print("No. of drinks selected = ", qty)
            elif choice == 'HM' or choice == 'hm':
                price = 1.2
                total += price
                qty += 1
                print("No. of drinks selected = ", qty)
            elif choice == 'IC' or choice == 'ic':
                price = 1.5
                total += price
                qty += 1
                print("No. of drinks selected = ", qty)
            elif choice == 'HC' or choice == 'hc':
                price = 1.2
                total += price
                qty += 1
                print("No. of drinks selected = ", qty)
            elif choice == '1P' or choice == '1p':
                price = 1.1
                total += price
                qty += 1
                print("No. of drinks selected = ", qty)
            elif choice == 'CC' or choice == 'cc':
                price = 1.3
                total += price
                qty += 1
                print("No. of drinks selected = ", qty)
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
                        if NoOf10.isnumeric():
                            NoOf10 = int(NoOf10)
                            TotalAmtOf10 = NoOf10*10
                            if TotalAmtOf10 >= total:
                                change = TotalAmtOf10 - total
                                print("Thank you! Please collect your change: $%.2f" % change)
                                print("Exiting Vending Machine")
                                purchasing = False
                                break
                            else:
                                while five:
                                    NoOf5 = input("Enter no. of $5 notes: ")
                                    if NoOf5.isnumeric():
                                        NoOf5 = int(NoOf5)
                                        TotalAmtOf5 = NoOf5*5
                                        check = TotalAmtOf5 + TotalAmtOf10
                                        if check >= total:
                                            change = check - total
                                            print("Thank you! Please collect your change: $%.2f" % change)
                                            print("Exiting Vending Machine")
                                            purchasing = False
                                            five = False
                                            ten = False
                                            break
                                        else:
                                            while two:
                                                NoOf2 = input("Enter no. of $2 notes: ")
                                                if NoOf2.isnumeric():
                                                    NoOf2 = int(NoOf2)
                                                    TotalAmtOf2 = NoOf2*2
                                                    check1 = check + TotalAmtOf2
                                                    if check1 >= total:
                                                        change = check1 - total
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
                    print("Exiting the Vending Machine! Good Bye!")
                    purchasing = False
                    break
            else:
                print("Invalid Choice")
    else:
        print("Invalid Option. Exiting Vending Machine")
