import os
os. system('cls')

bank_names = []
bank_balance = []

print('Enter the names and balances of bank accounts (type: quit when done) ')
acct_name = None

while acct_name != 'quit':
    acct_name = input('What is the name of the bank account? ')
    if acct_name != 'quit':
        acct_balance = float(input('What is the available balance? '))
        bank_names.append(acct_name)
        bank_balance.append(acct_balance)
print()

print('Account Informations:')
for index in range(len(bank_names)):
     print(f'{index}. {bank_names[index]} - {bank_balance[index]}')
print()

bank_total =  0
average = 0
for index in range(len(bank_names)):
    bank_total += bank_balance [index]
    average = bank_total/len(bank_names)
    
print (f'Total: ${bank_total:.2f} ')
print(f'Average: ${average:.2f}')

print()
highest_account_index = -1
highest_balance = 0
for index in range(len(bank_names)):
    if bank_balance[index] > highest_balance:
        highest_account_index = index
print(f'Highest balance: {bank_names[highest_account_index]} - {bank_balance[highest_account_index]}')        
print()

remove_acct_question = None
while remove_acct_question != "no":
    remove_acct_question = input('Do you want to update an account? yes or no ')
    if remove_acct_question.lower() == "yes":
        remove_acct = int(input('What account index do you want to update? '))
        acct_balance = float(input('What is your new amount? '))
        bank_balance[remove_acct] = acct_balance

print('Account Informations:')
for index in range(len(bank_names)):
     print(f'{index}. {bank_names[index]} - {bank_balance[index]}')