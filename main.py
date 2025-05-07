
from library import Book, Library, Student

lib = Library()

bk_1 = Book("Introduction to python", "Mayanja")
bk_2 = Book("Introduction to computer systems", "Muhammad", 3)

sdt_1 = Student("Jeema")
sdt_2 = Student("Kibirige")

lib.add_book(bk_1)
lib.add_book(bk_2)

print(lib.borrow_book("Introduction to python", sdt_2))
print(lib.borrow_book("Introduction to computer systems", sdt_2))
