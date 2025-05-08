class User:
    def __init__(self, name):
        self.name = name

class Book: #book class that creates the books in the library
    def __init__(self, title, author, number_of_copies = 1):
        self.title = title
        self.author = author
        self.number_of_copies = number_of_copies
        

class Library: #creates relationships btn books and students who borrow them
    def __init__(self):
        self.__books = []
        self.__borrowers = []
    
    def add_book(self, book):
        self.__books.append(book)
    
    def get_books(self):
        return self.__books

    def search_for_book(self, title):
        for book in self.__books:
            if book.title == title:
                return book
        
    def get_borrowers(self):
        return self.__borrowers
            
        return f"Book with title {title} doesn't exist--You might want to check the spelling and try again"
    
    def borrow_book(self, title, student):

        book = self.search_for_book(title)

        if isinstance (book, str):
            return book #for this case, the method, self.search_for_book returned an error message

        if self.__borrowers != []: #checking whether a student already has a book he hasnt returned b4 we give them a new one
            for borrower in self.__borrowers:
                if student.name == borrower.get("student").name:
                    return f"{borrower.get('student').name} already has a book, {borrower.get('book').title}"

        if book.number_of_copies > 0:
            
            self.__borrowers.append({"student":student,"book":book})

            if book.number_of_copies == 0:
                self.__books.remove(book)
            return "Please take your book"
        else:
            return f"{book.title} is out of stock"

class Student(User): #creates student objects that borrow the book
    def __init__(self, name, student_class):
        super().__init__(name)
        self.student_class = student_class
        
    def get_student_details(self):
        return f"Name:\t{self.name}\nClass:\t{self.student_class}"
    


