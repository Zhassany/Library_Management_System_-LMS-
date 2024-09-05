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
            raise ValueError("author's name must contain only letter and space")

    @property
    def isbn(self):
        return self.__isbn
    
    @isbn.setter
    def isbn(self, number):
        if number.isdigit():
            self.__isbn = number
        else:
            raise ValueError("isbn must contain only digit")

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
            raise ValueError("member's name must contain only letter and space")

    def __repr__(self):
        return '\nname: %-20s    member_id: %-20s\n' % (self.name, self.member_id)
    
    def borrow_book(self, book):
        if isinstance(book, Book):
            self.borrowed_books += [book]
            book._borrow()
        else:
            raise TypeError('input of borrow_book function must be an object of Book class')
    
    def return_book(self, book):
        self.borrowed_books.remove(book)
        book._return_book()

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        if isinstance(book, Book):
            if not (book.isbn in [x.isbn for x in self.books]):
                self.books += [book]
            else:
                raise AssertionError('this book has already been added')
        else:
            raise TypeError('input of add_book function must be an object of Book class')

    def register_member(self, member):
        if isinstance(member, Member):
            if not (member.member_id in [x.member_id for x in self.members]):
                self.members += [member]
            else:
                raise AssertionError('this member has already been registered')
        else:
            raise TypeError('input of register_member function must be an object of Member class')
    
    def issue_book(self, member_id, isbn):
        memberIsExist = False
        for member in self.members:
            if member.member_id == member_id:
                memberIsExist = True
                break
        
        bookIsExist = False
        for book in self.books:
            if book.isbn == isbn:
                bookIsExist = True
                break
        
        if memberIsExist:
            if bookIsExist:
                member.borrow_book(book)
            else:
                raise AssertionError(f'{isbn} has not been added to the library')
        else:
            raise AssertionError(f'{member_id} has not been registered to the library')
    
    def return_book(self, member_id, isbn):
        memberIsExist = False
        for member in self.members:
            if member.member_id == member_id:
                memberIsExist = True
                break
        
        bookIsExist = False
        for book in self.books:
            if book.isbn == isbn:
                bookIsExist = True
                break
        
        if memberIsExist:
            if bookIsExist:
                member.return_book(book)
            else:
                raise AssertionError(f'{isbn} not found')
        else:
            raise AssertionError(f'{member_id} not found')
