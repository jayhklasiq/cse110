import os
os.system('cls')


scriptures = []
books = []
chapters = []
largest = 0
largest_index = -1
with open('books_and_chapters.txt') as books_and_chapters:
    for data_line in books_and_chapters:
        data_line = data_line.strip().split(':')
        books.append(data_line[0])
        chapters.append(int(data_line[1]))
        scriptures.append(data_line[2])
#Find the largest number of chapters in the scriptures.
#Find the book that has the largest number of chapters in the scriptures.
largest_number_of_chapters = chapters.index(max(chapters))
print(f'With {chapters[largest_number_of_chapters]} chapters, the book of {books[largest_number_of_chapters]} in the {scriptures[largest_number_of_chapters]} has the largest number of chapters in the volume of scriptures.')

print()
for index in range(len(scriptures)):
    if scriptures[index] == "Book of Mormon":
        #Change your program so that it only prints the books in the Book of Mormon.
        print (f'{books[index]}')

#Find the book in the Book of Mormon that has the largest number of chapters
for index in range(len(scriptures)):
    if scriptures[index] == "Book of Mormon"and chapters[index] > largest:
        largest = chapters[index]
        largest_index = index
        print()
print(f'The largest number of chapters in the "Book of Mormon" is {books[index]} with {chapters[index]}')
#At the beginning of the program, ask the user which volume of scriptures they would like to learn about (for example, Old Testament, New Testament, Book of Mormon, Doctrine and Covenants, Pearl of Great Price). 
#Then, find the book in that volume of scripture that has the largest number of chapters.
print('So, tell me. What volume of scripture would you like to read today? \n A. Old Testament \n B.New Testament \n C. Book of Mormon \n D. Doctrine and Covenants \n E. Pearl of Great Price')
volume_of_scriptures = ['Old Testament','New Testament','Book of Mormon','Doctrine and Covenants','Pearl of Great Price']
for index in range(len(volume_of_scriptures)):
  print(f"{index + 1}. {volume_of_scriptures[index]}")

volume_of_scripture = int(input("Please select a volume of scripture: "))

for index in range(len(scriptures)):
    if scriptures[index] == volume_of_scriptures[volume_of_scripture - 1] and chapters[index] > largest:
        largest = chapters[index]
        largest_index = index
print(f'The book with the largest chapter is {books[largest_index]} with chapters {chapters [largest_index]}')