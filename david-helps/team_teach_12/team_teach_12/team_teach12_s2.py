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

# Stretch Challenge #2
# Find the book in the Book of Mormon that has the largest number of chapters
for index in range(len(scriptures)):
  if(scriptures[index] == "Book of Mormon" and chapters[index] > largest):
    largest = chapters[index]
    largest_index = index

print(f"The book with the largest number of chapter is {books[largest_index]} with {chapters[largest_index]} chapters")