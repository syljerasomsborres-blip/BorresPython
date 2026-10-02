while True:
    borres_flavor = input("Choose Flavor (Hawaiian/Pepperoni/Cheese): ").lower()
    borres_quantity = float(input("Quantity: "))

    match borres_flavor:
        case "hawaiian":
            borres_size = input("Choose Size (Small/Medium/Large): ").lower()
            if borres_size == "small":
                borres_price = 250
            elif borres_size == "medium":
                borres_price = 350
            elif borres_size == "large":
                borres_price = 450
            else:
                print("Invalid Size")

        case "pepperoni":
            borres_size = input("Choose Size (Small/Medium/Large): ").lower()
            if borres_size == "small":
                borres_price = 300
            elif borres_size == "medium":
                borres_price = 400
            elif borres_size == "large":
                borres_price = 500
            else:
                print("Invalid Size")

        case "cheese":
            borres_size = input("Choose Size (Small/Medium/Large): ").lower()
            if borres_size == "small":
                borres_price = 150
            elif borres_size == "medium":
                borres_price = 250
            elif borres_size == "large":
                borres_price = 350
            else:
                print("Invalid Size")

        case _:
            print("Invalid Flavor")

    borres_amount = borres_quantity * borres_price
    print("Amount: ", borres_amount)

    again = input("Do you want to order again? (Y/N): ")

    if again.upper() != "Y":
        print("Order is Complete.")
        break

