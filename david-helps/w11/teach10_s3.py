# -----------------------------------------------------------
# Lists
# Demonstrate your understanding of multiple lists
#
# David Ward
# CSE 110 Section 22
# ----------------------------------------------------------- 

# EXTRA - Clears the terminal before the game is played
import os
os.system('clear')

# Requirement 1
account_names = []
account_balances = []
account_name = ""
print("Enter the names and balances of bank accounts (type: quit when done)")

while(account_name != "quit"):
  account_name = input("What is the name of this account? ")
  if(account_name != "quit"):
    account_balance = float(input("What is the balance? "))
    account_names.append(account_name)
    account_balances.append(account_balance)

# Requirement 2
total_balance = 0
print("\nAccount Information:")
for i in range(len(account_names)):
  total_balance += account_balances[i]
  print(f"{i}. {account_names[i]} - ${account_balances[i]:.2f}")

# Requirement #3
print(f"\nTotal: ${total_balance}")
print(f"Average: ${(total_balance / len(account_names)):.2f}")

# Stretch Challenge 1
highest_balance_index = -1
highest_balance = 0
for i in range(len(account_balances)):
  if(account_balances[i] > highest_balance):
    highest_balance_index = i
print(f"Highest balance: ${account_names[highest_balance_index]} - ${account_balances[highest_balance_index]:.2f}")

# Stretch Challenge 3
# Change the last step into a loop, so that the user can keep updating accounts until 
# they say no. After each update, display the new list of balances.
change_an_account = None
while(change_an_account != "no"): 
  change_an_account = input("\nDo you want to update an account (yes or no)? ")
  if(change_an_account == "yes"):
    index_of_account = int(input("What account index do you want to update? "))
    account_balance = float(input("What is the new amount? "))
    account_balances[index_of_account] = account_balance

  print("\nAccount Information:")
  for i in range(len(account_names)):
    print(f"{i}. {account_names[i]} - ${account_balances[i]:.2f}")
