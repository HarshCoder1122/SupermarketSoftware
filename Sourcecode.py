def add_product():
    product_list = {}
    while True:
        pro = input("Press A to Add Product or Press Q to exit: ")
        if pro == "A":
            product_name = input("Enter The Name Of the Product: ")
            while True:
                try:
                    product_quantity = int(input("Enter The Quantity of the Product: "))
                    break
                except ValueError:
                    print("Please enter a valid quantity.")
            product_list[product_name.title()] = product_quantity
            print(f"{product_name.title()} added to the list.")
        elif pro == "Q":
            break
        else:
            print("Please Select a valid Command!!! ")
    return product_list

def get_price(product_list):
    price_list = {
        "Onion": 35,
        "Potato": 40,
        "Cashew": 120,
        "Almond": 125,
        "Garlic": 69,
        "Tomato": 69,
        "Ginger": 55,
        "Hair Oil": 89,
        "Carrot": 45,
        "Cabbage": 30,
        "Spinach": 25,
        "Banana": 20,
        "Apple": 60,

        }
    total = 0
    for product, quantity in product_list.items():
        if product in price_list:
            subtotal = price_list[product] * quantity
            print(f"{product}: ₹{price_list[product]} X {quantity} = ₹{subtotal}")
            total += subtotal
        else:
            print(f"{product} Out of stock.Sorry for inconvinience!!!")
    print(f"Total: ₹{total}")
    return total

def discount(total):
    member=input("Enter A for GOLD\nEnter B for SILVER\nEnter C for BRONZE\nEnter D for not a Member: ").upper()
    if member=="A":
        totalmoney=total-(20/100)*total
    elif member=="B":
        totalmoney=total-(10/100)*total
    elif member=="C":
        totalmoney=total-(5/100)*total
    else:
        totalmoney=total
    print(f"Total after discount: ₹{totalmoney}")
    return totalmoney

def payment_type(totalmoney):
    payment=input("Enter A for CARDS\nEnter B for UPI\nEnter C for CASH: ").upper()
    if payment=="A":
        print(f"Payment of ₹{totalmoney} recieved via CARD")
    elif payment=="B":
        print(f"Payment of ₹{totalmoney} recieved via UPI")
    elif payment=="C":
        print(f"Payment of ₹{totalmoney} recieved via CASH")
    else:
        print("Transaction failed!!!")

product_list = add_product()
total = get_price(product_list)
totalmoney = discount(total)
payment_type(totalmoney)