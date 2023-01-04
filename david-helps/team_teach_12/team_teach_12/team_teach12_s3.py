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

# Stretch Challenge #3
# At the beginning of the program, ask the user which volume of scriptures they would
# like to learn about (for example, Old Testament, New Testament, Book of Mormon, 
# Doctrine and Covenants, Pearl of Great Price). Then, find the book in that volume of 
# scripture that has the largest number of chapters.

# Display numeric choices because we cannot be certain someone will type the full
# name of the scripture volume
choices = ["Old Testament", "New Testament", "Book of Mormon", "Doctrine and Covenants", "Pearl of Great Price"]

# Display the list of choices
for index in range(len(choices)):
  print(f"{index + 1}. {choices[index]}")

# Get user input
choice = int(input("Please select a volume of scripture: "))

# Find the book with the largest number of chapters in the volume selected by the user
for index in range(len(scriptures)):
  # if the volume of scripture equals the user's choice AND the number of chapters in the book is the largest
  if(scriptures[index] == choices[choice - 1] and chapters[index] > largest):
    largest = chapters[index]
    largest_index = index

print(f"The book with the largest number of chapter is {books[largest_index]} with {chapters[largest_index]} chapters")