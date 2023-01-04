import os
os.system ('cls')

def display_message(message):
  print (message)

def display_msg_in_uppercase(message):
  message = user_msg.upper()
  print (message)

def display_msg_in_lowercase(message):
  message = user_msg.lower()
  print (message)

user_msg = input ('What is your message? ')
print()

display_message(user_msg)
display_msg_in_uppercase(user_msg)
display_msg_in_lowercase(user_msg)