
class Book: #book class that creates the books in the library
    def __init__(self, title, author, number_of_copies = 0):
        self.title = title
        self.author = author
        self.number_of_copies = number_of_copies
        

class Library: #creates relationships btn books and students who borrow them
    def __init__(self):
        self.books = []
        self.borrowers = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def get_books(self):
        return self.books

    def search_for_book(self, title):
        for book in self.books:
            if book.title == title:
                
                return book
            else:
                return f"Book with title {title} doesn't exist"
    
    def borrow_book(self, title, student):

        book = self.search_for_book(title)

        if isinstance (book, str):
            return book #for this case, the method, self.search_for_book returned an error message

        if self.borrowers != []: #checking whether a student already has a book he hasnt returned b4 we give them a new one
            for borrower in self.borrowers:
                if student.name == borrower.get("student").name:
                    return f"{borrower.get('student').name} already has a book, {borrower.get('book').title}"

        if book.number_of_copies > 0:
            
            self.borrowers.append({"student":student,"book":book})

            if self.number_of_copies == 0:
                self.books.remove(book)
            return "Please take your book"
        else:
            return f"{book.title} is out of stock"



class Student: #creates student objects that borrow the books
    def __init__(self, name):
        self.name = name
    
    def get_student_details(self):
        return self.name

