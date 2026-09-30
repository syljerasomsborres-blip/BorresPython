print("========== PIZZA MENU CALCULATOR ============")
borresflavor = input("Hawaiian/Pepperoni/Cheese \nPick A Flavor: ").lower()
borressize = input("Small/Medium/Large \nPick Size: ").lower()
borresquantity = int(input("Quantity: "))

match borresflavor:
    case "hawaiian":
        if borressize == "small":
            borresprice=250
        elif borressize == "medium":
            borresprice=350
        elif borressize == "large":
            borresprice=450
        else:
            borresprice=0
            print("Invalid Size")

    case "pepperoni":
        if borressize == "small":
            borresprice = 150
        elif borressize == "medium":
            borresprice = 250
        elif borressize == "large":
            borresprice = 350
        else:
            borresprice = 0
            print("Invalid Size")

    case "cheese":
        if borressize == "small":
            borresprice = 175
        elif borressize == "medium":
            borresprice = 275
        elif borressize == "large":
            borresprice = 375
        else:
            borresprice = 0
            print("Invalid Size")

    case _:
        print("Invalid Flavor")

borrestotal = borresprice * borresquantity
print(f"Total Amount: {borrestotal:,.2f}")
