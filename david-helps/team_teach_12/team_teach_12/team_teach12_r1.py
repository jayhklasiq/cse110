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

# Requirement #1
# Open the file, read through it line by line, separate the line into the 
# appropriate pieces and display each book in this format:
# Scripture: Old Testament, Book: Genesis, Chapters: 50
with open("w12/team_teach_12/books_and_chapters.txt") as scriptures_file:
  for line in scriptures_file:
    line_sections = line.split(":")
    books.append(line_sections[0])
    chapters.append(line_sections[1])
    scriptures.append(line_sections[2].strip())
    print(f"Scripture: {line_sections[2].strip()}, Book: {line_sections[0]}, Chapters: {line_sections[1].strip()}")