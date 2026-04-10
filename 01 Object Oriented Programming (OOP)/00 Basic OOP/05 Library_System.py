class Library:
    def __init__(self):
        self.books = []  
    def add_book(self, book_name):
        self.books.append(book_name)
        print(f"Book '{book_name}' added successfully!")
    def remove_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"Book '{book_name}' removed successfully!")
        else:
            print(f"Book '{book_name}' not found in the library.")
    def list_books(self):
        if self.books:
            print("Books in the library:")
            for idx, book in enumerate(self.books, 1):
                print(f"{idx}. {book}")
        else:
            print("No books in the library.")
library = Library()
library.add_book("Python Programming")
library.add_book("Data Structures")
library.list_books()
library.remove_book("Data Structures")
library.list_books()