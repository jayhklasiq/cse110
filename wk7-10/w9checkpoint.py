import os
os.system('cls')

friends = []
name_of_friends = ''

while name_of_friends != 'end':
    name_of_friends = input('What are your friends name? ')
    
    if name_of_friends != 'end':
        friends.append(name_of_friends)
    
for names in friends:
    print(names)