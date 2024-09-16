# OOPlaboratoare-
laborator 1 
# Simple Library Management System

This Python project features a basic library management system with two classes: `Book` and `Library`.

## Files

- **`book.py`**: Defines the `Book` class with attributes for title, author, and ISBN.
- **`library.py`**: Defines the `Library` class for managing books—adding, removing, and listing them.

## Classes

### Book

Represents a book with:
- **`title`**: The book's name.
- **`author`**: The book's author.
- **`isbn`**: A unique identifier.

Methods:
- **`__init__`**: Creates a new book.
- **`__str__`**: Returns book details as a string.

### Library

Manages a collection of books.

Methods:
- **`__init__`**: Initializes an empty library.
- **`add_book`**: Adds a book.
- **`remove_book`**: Removes a book by ISBN.
- **`display_books`**: Lists all books.

## Usage Example

```python
from book import Book
from library import Library

library = Library()
book1 = Book("1984", "George Orwell", "1234567890")
book2 = Book("Pride and Prejudice", "Jane Austen", "0987654321")

library.add_book(book1)
library.add_book(book2)

print("Books in the library:")
library.display_books()

if library.remove_book("1234567890"):
    print("\nBook removed.")
else:
    print("\nBook not found.")

print("\nBooks after removal:")
library.display_books()
