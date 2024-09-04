class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.__available = True
    
    @property
    def author(self):
        return self.__author
    
    @author.setter
    def author(self, name):
        if all(ch.isalpha() or ch.isspace() for ch in name):
            self.__author = name
        else:
            raise ValueError("The author's name must contain only letter and space")

    @property
    def isbn(self):
        return self.__isbn
    
    @isbn.setter
    def isbn(self, number):
        if number.isdigit():
            self.__isbn = number
        else:
            raise ValueError("The isbn must contain only digit")

    def __repr__(self):
        return '\ntitle: %-20s    author: %-20s\n' % (self.title, self.author)

    def _borrow(self):
        if self.__available:
            self.__available = False
        else:
            raise AssertionError(f'{self.title} is not available') 

    def _return_book(self):
        if not self.__available:
            self.__available = True
        else:
            raise AssertionError(f'{self.title} is already available')
        
class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name_inp):
        if all(ch.isalpha() or ch.isspace() for ch in name_inp):
            self.__name = name_inp
        else:
            raise ValueError("The member's name must contain only letter and space")

    def __repr__(self):
        return '\nname: %-20s    member_id: %-20s\n' % (self.name, self.member_id)
    
    def borrow_book(self, book):
        if isinstance(book, Book):
            self.borrowed_books += [book]
            book._borrow()
        else:
            raise TypeError('The input of the borrow_book function must be an object of the Book class')
    
    def return_book(self, book):
        self.borrowed_books.remove(book)
        book._return_book()
