# -----------------------------------------------------------
# Iterating Through Strings
#
# David Ward
# CSE 110 Section 22
# ----------------------------------------------------------- 
import os

# EXTRA - Clears the terminal before the game is played
os.system('clear')

# # Stretch Requirement #1
# # instead of your program asking for a favorite letter, have it asks for a 
# # number n. Make the program capitalize every n-th letter in the string
nth_number = int(input("Please enter a number: "))
modified_quote = ""
quote = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."
# create new string
for i, letter in enumerate(quote):
  if((i % (nth_number + 1)) == 0):
    modified_quote += letter.upper()
  else:
    modified_quote += letter
print(modified_quote)

# # Stretch Requirement #1 - modifying list 
# # first - convert string to list
# quote_list = list(quote)

# # second loop through string like normal - # look at every n-th letter
# for i, letter in enumerate(quote):
#   if((i % (nth_number + 1)) == 0):

#     #third - replace each letter in n-th position in lst with uppercase letter
#     quote_list[i] = quote_list[i].upper()

# # print results
# # str().join() converts list back to a string
# print(str().join(quote_list))
