import os
os. system('cls')

shopping_items = []

print('Please enter the items of the shopping list (type: quit to finish):')
items = ''
while items != 'quit':
    items = input('Item: ')
    if items != 'quit':
        shopping_items.append(items)
print()
print(f'Your shopping list is:')
for item in shopping_items:
    print(item)
# this function print the index numbers next to the elements of the list as you iterate through
print()
print('The shopping list with indexes is:')
for i in range(len(shopping_items)):
    item = shopping_items[i]
    print(f'{i}. {item}')       

print()
item_to_change = int(input('Which item will you like to change? '))
new_item = input('What is the new item you want to add? ')

shopping_items[item_to_change] = new_item

print()
print('The shopping list with indexes is:')
for i in range(len(shopping_items)):
    item = shopping_items[i]
    print(f'{i}. {item}')