class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True
    
    @property
    def author(self):
        return self.__author
    
    @author.setter
    def author(self, name):
        if all(ch.isalpha() or ch.isspace() for ch in name):
            self.__author = name
        else:
            raise ValueError("The author's name must contain only letters and space")

    @property
    def isbn(self):
        return self.__isbn
    
    @isbn.setter
    def isbn(self, number):
        if number.isdigit():
            self.__isbn = number
        else:
            raise ValueError("The isbn must contain only digits")

    
    def __str__(self):
        return f'title: {self.title}    author: {self.author}'

    def borrow(self):
        if self.available:
            self.available = False
        else:
            raise AssertionError(f'{self.title} is not available') 

    def return_book(self):
        if not self.available:
            self.available = True
        else:
            raise AssertionError(f'{self.title} is already available')