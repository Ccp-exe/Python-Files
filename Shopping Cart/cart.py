item =input("What item would you like to buy?: ")
price= float (input("Enter the price: "))
quantity= int(input("How many would you like?: "))

total= price*quantity
print(f"Your total for {quantity} {item} is ${total} Cash or Card?")