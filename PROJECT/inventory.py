inventory = {
    "Rice": 25,
    "Beans": 5,
    "Milk": 10,
    "Bread": 8
}

#Display all products and quantities.
# print(inventory)
print()
print("--------------- Inventory ---------------")
for key,value in inventory.items():
    print(f"{key} => {value}")
print("-----------------------------------------")



#Ask the user for a product name.
# If the product exists:
# Show its quantity.
while True:
    product = input("Enter product: ").strip().capitalize()
    if inventory.get(product):
        print(f"{product} is available")
        print(f"Quantity => {inventory[product]}")
    else:
        print(f"{product} is not available")


    #Ask the user if they want to add stock.
    print("Do you want to add stock?")
    choice = input("(y/n): ").strip().lower()
    if choice == 'y':
        prod = input("Enter product: ").strip().capitalize()
        if inventory.get(prod):
            quantity = int(input("Quantity to add: ").strip())
            inventory[prod] +=quantity
            print("Quantity added!")
            print(f"Updated inventory => {prod}:{inventory[prod]}")

    else:
        print("Alright then!")
        break

#Find items with the quantity below 10
minimum_quant = 10 #1 - 9, 
item_key = None
minimum_qntties = []
total_stocks = []
total_qntties = []

for key, value in inventory.items():   #4 items 1 2 3 4
    total_stocks.append(key)
    total_qntties.append(value)
    if value < minimum_quant:
        minimum_quant_quant = value
        item_key = key
        minimum_qntties.append(item_key)

print(f"Total stock item: {len(total_stocks)}")
print(f"Total Quantities: {sum(total_qntties)}")
print(f"Products with quantity less than 10: {minimum_qntties}")