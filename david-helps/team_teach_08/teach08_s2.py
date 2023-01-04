# -----------------------------------------------------------
# Iterating Through Strings
#
# David Ward
# CSE 110 Section 22
# ----------------------------------------------------------- 
import os

# EXTRA - Clears the terminal before the game is played
os.system('clear')

# Stretch Requirement #2
# Same as #1, but continue while user enters 'yes' to continue
again = "yes"
quote = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."
# create new string
while(again == "yes"):
  modified_quote = ""
  nth_number = int(input("Please enter a number: "))
  for i, letter in enumerate(quote):
    if((i % (nth_number + 1)) == 0):
      modified_quote += letter.upper()
    else:
      modified_quote += letter
  print(modified_quote)
  again = input("Would you like to enter another number? ").lower()