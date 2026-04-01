item1= input('name of item: ')
item2= input('name of item: ')
item3= input('name of item: ')
price1= float(input('price of item1: '))
price2= float(input('price of item2: '))
price3= float(input('price of item3: '))
quantity1= int(input('Enter quantity of item1: '))
quantity2= int(input('Enter quantity of item2: '))
quantity3= int(input('Enter quantity of item3: '))
total_price1= price1 * quantity1
total_price2= price2 * quantity2
total_price3= price3 * quantity3
total= total_price1 + total_price2 + total_price3
print(f'Summary for your shopping item is:')
print(f'{item1}: {price1} x {quantity1} : £{total_price1}')
print(f'{item2}: {price2} x {quantity2} : £{total_price2}')
print(f'{item3}: {price3} x {quantity3} : £{total_price3}')
print(f'subtotal: £{total}')
