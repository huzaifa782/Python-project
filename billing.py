bill = {}


while True: 
    item = input("Enter The item:   ")
    price = int(input("Enter The Price:  "))
    bill.update({item   :   price})
    ask = input("Press x for total amount or just press enter to continue:  ")


    if ask.lower() == "x":
        print("Grocery Item\n")
        print("item            Quantity")
        print("-------------------------")

        for item, quantity in bill.items():
            print(f"{item.ljust(12)}  {quantity}")
        total = sum(bill.values())
        print("--------------------------")
        print("Total".ljust(12), total)

        break

    else:
        continue


