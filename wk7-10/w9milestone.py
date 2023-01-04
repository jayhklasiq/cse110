import os
os. system('cls')

print('Welcome to MoRewa Shopping Cart Program')
start = int(input('Please select one of the following: \n 1. Add Item \n 2. View Cart \n 3. Remove Item \n 4. Compute total \n 5. Quit \n Please input an action: '))

#req 02
shopping_list = []
shopping_item_prize = []

#req 01
while start != 5:
    if start == 1 and start != 5:
        shopping_items = input('What item would you like to add to your cart? ')
        item_prize = float(input('How much is it? '))
        shopping_list.append(shopping_items)
        shopping_item_prize.append(item_prize)
        print(f'{shopping_items} has been added to cart.')
        print()
    elif start == 2:
        print('Here are the items in your cart:')
        for index in range(len(shopping_list)):
            print(f'{index + 1}. {shopping_list[index]} - ${shopping_item_prize[index]}')
        print()
    elif start == 3:
        remove_an_item = int(input('What item number? '))
        shopping_list.pop(remove_an_item - 1)
        shopping_item_prize.pop(remove_an_item -1)
        print('Item removed')
        print()
    elif start == 4:
        cart_total_cost = 0
        for cost in range(len(shopping_item_prize)):
            cart_total_cost += shopping_item_prize[cost]
        print(f'Total prize of the items in your cart is : ${cart_total_cost}')
        print()                                                                                                                                                                                          
    start = int(input('Please select one of the following: \n 1. Add Item \n 2. View Cart \n 3. Remove Item \n 4. Compute total \n 5. Quit \n Please input an action: '))
print('Thank you for using MoRewa.')

    