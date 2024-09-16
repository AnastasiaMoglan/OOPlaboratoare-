class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if not isinstance(book, Book):
            print("Error: You need to add a Book object.")
            return
        self.books.append(book)

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                return True
        return False

    def display_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            for book in self.books:
                print(book)

if __name__ == "__main__":
    library = Library()
    
    book1 = Book("1984", "George Orwell", "1234567890")
    book2 = Book("Pride and Prejudice", "Jane Austen", "0987654321")
    
    library.add_book(book1)
    library.add_book(book2)
    
    print("Books in the library:")
    library.display_books()

    if library.remove_book("1234567890"):
        print("\nBook removed successfully.")
    else:
        print("\nBook not found.")
    
    print("\nBooks after removal:")
    library.display_books()
