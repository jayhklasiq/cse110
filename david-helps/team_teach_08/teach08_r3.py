# -----------------------------------------------------------
# Iterating Through Strings
#
# David Ward
# CSE 110 Section 22
# ----------------------------------------------------------- 
import os

# EXTRA - Clears the terminal before the game is played
os.system('clear')

# Requirement #3
# Change the program, so that instead of capitalizing the user's favorite 
# letter, it "hides" it, and replaces it with an underscore in the display
word = "Commitment"
favorite_letter = input("What is your favor letter? ").lower()
for letter in word:
  if(letter.lower() == favorite_letter):
    print("_", end = "")
  else:
    print(f"{letter}", end = "")
print("\n")
