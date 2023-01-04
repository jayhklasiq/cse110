# -----------------------------------------------------------
# Iterating Through Strings
#
# David Ward
# CSE 110 Section 22
# ----------------------------------------------------------- 
import os

# EXTRA - Clears the terminal before the game is played
os.system('clear')

# Requirement #1 
# Write code that loops through the word letter by letter. 
# If the letter is "m", print it as a capital letter. If the
# letter is anything else, print it out as a lowercase letter.
print("Requirement #1")
word = "Commitment"
for letter in word:
  if(letter.lower() == "m"):
    print(f"{letter.upper()}")
  else:
    print(f"{letter}")

# Requirement #2 
# Change the print statements so that each letter is not printed 
# on its own line, but rather they are printed out next to each 
# other on the same line
#
# Also, change the program to allow the user to specify the letter 
# (rather than always using "m"). Make sure your program matches 
# the letter in the word, regardless of whether the user entered it 
# as a capital or lowercase, and regardless of whether that letter 
# was a capital or lowercase in the original word
print("\n\nRequirement #2")
favorite_letter = input("What is your favor letter? ").lower()
for letter in word:
  if(letter.lower() == favorite_letter):
    print(f"{letter.upper()}", end = "")
  else:
    print(f"{letter}", end = "")

# Requirement #3
# Change the program, so that instead of capitalizing the user's favorite 
# letter, it "hides" it, and replaces it with an underscore in the display
print("\n\nRequirement #3")
favorite_letter = input("What is your favor letter? ").lower()
for letter in word:
  if(letter.lower() == favorite_letter):
    print("_", end = "")
  else:
    print(f"{letter}", end = "")

# # Stretch Requirement #1
# # instead of your program asking for a favorite letter, have it asks for a 
# # number n. Make the program capitalize every n-th letter in the string
print("\n\nStretch Requirement #1")
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

# Stretch Requirement #1 - modifying list 
# first - convert string to list
print("\n\nStretch Requirement #1 - Done differently - Same results")
quote_list = list(quote)

# second loop through string like normal - # look at every n-th letter
for i, letter in enumerate(quote):
  if((i % (nth_number + 1)) == 0):

    #replace each letter in n-th position in lst with uppercase letter
    quote_list[i] = quote_list[i].upper()

# print results
# str().join() converts list back to a string
print(str().join(quote_list))

# Stretch Requirement #2
# Same as #1, but continue while user enters 'yes' to continue
print("\n\nStretch Requirement #2")
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