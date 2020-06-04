# shopping_cart.py

from os import system, name
import datetime

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

# TODO: write some Python code here to produce the desired output

#print(products)

def clear(): # clear the screen
        _ = system('clear')


def calc_tax(subtotal):
    return (1.0875*subtotal)

def calc_total(subtotal, tax):
    return (subtotal+tax)

def print_receipt(products, scan_items): #print the reciept
    
    output_string =''

    print('\n*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+**\n')
    output_string += '\n*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+**\n'

    print('                                 LEAN GREEN GROCERY MACHINE')
    output_string +='                                 LEAN GREEN GROCERY MACHINE\n'
    print('                             WWW.LEAN-GREEN-GROCERY-MACHINE.COM')
    output_string +='                             WWW.LEAN-GREEN-GROCERY-MACHINE.COM\n'

    print('\n*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+**\n')
    output_string +='\n*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+**\n'

    print('                            CHECKOUT AT:',(datetime.datetime.now()))
    output_string += '                            CHECKOUT AT:' + str(datetime.datetime.now())
    output_string += '\n'

    print('\n*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+**\n')
    output_string += '\n*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+**\n'

    subtotal = 0
    num = 0
    print('SELECTED PRODUCTS:\n')
    output_string += 'SELECTED PRODUCTS:\n'

    for i in scan_items:
        num = num + 1
        matched_ids = [p for p in products if str(p['id']) == str(i)]
        catalog_item = matched_ids[0]
        subtotal = subtotal + catalog_item['price']
        print(str(num)+'. '+catalog_item['name']+' '+'$'+str(catalog_item['price']))
        output_string += str(num)+'. '+catalog_item['name']+' '+'$'+str(catalog_item['price'])
        output_string += '\n'

    print('\n*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+**\n')
    output_string +='\n*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+**\n'

    tax = calc_tax(subtotal)
    total = calc_total(subtotal, tax)
    tax = to_usd(tax)
    total = to_usd(total)

    print('SUBTOTAL:',to_usd(subtotal))
    output_string += 'SUBTOTAL:' + to_usd(subtotal)
    output_string += '\n'
    print('TAX:     ',tax)
    output_string += 'TAX:     '+ tax
    output_string += '\n'
    print('TOTAL:   ',total)
    output_string +='TOTAL:   '+ total
    output_string += '\n'

    print('\n*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+**\n')
    output_string += '\n*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+**\n'
    
    print('                                  THANKS, SEE YOU AGAIN SOON!')
    output_string += '                                  THANKS, SEE YOU AGAIN SOON!\n'
    
    print('\n*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+**\n')
    output_string += '\n*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+**\n'

    return output_string

def get_items(opt):
    identifier = input('Please input a product identifer or DONE to finish:')
    
    if str(identifier) not in opt:
        clear()
        print("You selected an item to check out that is not in the store - Are you trying to reverse shoplift??")
        quit()

    item_list = []

    while identifier != "DONE":
        item_list.append(identifier)
        identifier = input('Please input a product identifer or DONE to finish:')
        if str(identifier) not in opt:
            print("You selected an item to check out that is not in the store - Are you trying to reverse shoplift??")
            quit()

    return item_list    

if __name__ == "__main__":

    clear()
    
    options = [str(i['id']) for i in products]
    options.append('DONE')

    items = get_items(options)

    with open("E-Reciept.txt",'w') as file:
        file.write(print_receipt(products,items))
    
    print('\nA new e-reciept was also created and stored in your current directory for you convienence! Enjoy!\n')

   