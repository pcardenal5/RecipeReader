from src.Book import Book

book1 = Book(path = './data/Arzak.pdf')
with open('./data/Arzak.txt', 'w') as oputputFile:
    oputputFile.write(book1.read())