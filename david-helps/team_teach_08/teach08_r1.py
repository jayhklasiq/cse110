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
word = "Commitment"
for letter in word:
  if(letter.lower() == "m"):
    print(f"{letter.upper()}")
  else:
    print(f"{letter}")
print()
