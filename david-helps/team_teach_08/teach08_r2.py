# -----------------------------------------------------------
# Iterating Through Strings
#
# David Ward
# CSE 110 Section 22
# ----------------------------------------------------------- 
import os

# EXTRA - Clears the terminal before the game is played
os.system('clear')

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
word = "Commitment"
favorite_letter = input("What is your favor letter? ").lower()
for letter in word:
  if(letter.lower() == favorite_letter):
    print(f"{letter.upper()}", end = "")
  else:
    print(f"{letter}", end = "")
print("\n")
