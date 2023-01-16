'''
    Stub class to create books to test the wrappers functionality.
    Attributes: 
                title := Booktitle
                author := Book's author
                language := Book's language
                isbn := Book's isbn (dublicate)
'''
import random
import string


class Stub_Book:
    title = None
    author = None
    language = None
    #isbn as dublicate (only for completion in stub class)
    isbn = None
    
    def __init__(self, title, author, language, isbn):
        self.title = title
        self.author = author
        self.language = language
        self.isbn = isbn

    def printAttr(self):
        print("Booktitle: ", self.title)
        print("Bookauthor: ", self.author)
        print("Booklanguage: ", self.language)
        print("Book's ISBN': ", self.isbn)

    

'''Stub function to return book object with isbn'''

def get_book_info(isbn):
    letters = string.ascii_lowercase

    book = Stub_Book(''.join(random.choice(letters) for i in range(10)), ''.join(random.choice(letters) for i in range(10)), ''.join(random.choice(letters) for i in range(10)), isbn)
    return book