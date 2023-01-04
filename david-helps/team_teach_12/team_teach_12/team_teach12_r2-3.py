# -----------------------------------------------------------
# Finding Items in a File
# Demonstrate your understanding of lists and indexes
#
# David Ward
# CSE 110 Section 22
# ----------------------------------------------------------- 


# EXTRA - Clears the terminal before the game is played
import os
os.system('clear')

# define and initialize variables
scriptures = []
books = []
chapters = []
largest = 0
largest_index = -1

with open("w12/team_teach_12/books_and_chapters.txt") as scriptures_file:
  index = -1
  for line in scriptures_file:
    index += 1
    line_sections = line.split(":")
    scriptures.append(line_sections[2].strip())
    books.append(line_sections[0])
    chapters.append(int(line_sections[1]))

    # Requirement #2 & #3 - The long way
    # Find the largest number of chapters in the scriptures
    # You could do within the loop this way, but there's a better way
    if(int(line_sections[1]) > largest):
      largest = int(line_sections[1])
      largest_index = index

# Requirement #2 & #3 - The long way (continued)
print(f"The largest number of chapters is {chapters[largest_index]} in the book of {books[largest_index]} in the {scriptures[largest_index]}")

# Requirement #2 & #3 - The better way
# Find the largest number of chapters in the scriptures
# A Better way - Use the max() function to get the largest values
# in the "chapters" list. This will give you the value in the list
max_value = max(chapters)

# Then, use index() function to get the index of the smallest value
largest_index = chapters.index(max_value)

# Then, use the index to print the entire set of values
print(f"The largest number of chapters is {chapters[largest_index]} in the book of {books[largest_index]} in the {scriptures[largest_index]}")