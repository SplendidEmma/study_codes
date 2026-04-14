items = [] # This is an empty list that will hold the items
prices = []
quantities = []
totals = []
grandtotal = 0
item = ""

while item != 'end': # when end is inputed, it will stop the loop
    item = input("Enter Item: ")
    if item != 'end':
        price = float(input(f"Enter price for {item}: "))
        quantity = int(input(f"Enter quantity of {item}: "))
        total = (price * quantity)
        grandtotal += (total)

        items.append(item)
        prices.append(price)
        quantities.append(quantity)
        totals.append(total)
        
if len(items) > 0: # this will cause printing only if theres an input for the item
    i = 0 # this is used for iteration to index the list
    print("")
    print("**************** RECEIPT ******************")
    print("") # this print a space(empty line) 
    
    while i < len(items):
        print(f"{items[i]}: £{prices[i]:.2f} x {quantities[i]}: £{totals[i]:.2f}")
        i+=1
    print("")
    print(f"Grand Total: £{grandtotal:.2f}")
    print("")
    print("*******************************************")