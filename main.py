
from library import Book, Library, Student, User

lib = Library()

bk_1 = Book("Introduction to python", "Mayanja")
bk_2 = Book("Introduction to computer systems", "Muhammad")

sdt_1 = Student("Jeema", "P2")
sdt_2 = Student("Kibirige", "P5")

lib.add_book(bk_1)
lib.add_book(bk_2)

print(lib.get_books())

print(lib.borrow_book("Introduction to python", sdt_2))
print(lib.borrow_book("Introduction to computer systems", sdt_1))

print(sdt_2.get_student_details())
