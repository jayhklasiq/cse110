import os
os.system ('cls')


# books_of_mormon = open('books.txt')

with open('books.txt') as books_of_mormon:
    for book in books_of_mormon:
        book = book.strip()
        print(book)