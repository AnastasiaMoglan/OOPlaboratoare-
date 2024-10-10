class Publication:
    def __init__(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def get_info(self):
        raise NotImplementedError("This method should be overridden by subclasses.")


class Book(Publication):
    def __init__(self, title, author, isbn):
        super().__init__(title)
        self.author = author
        self.isbn = isbn

    def get_author(self):
        return self.author

    def get_isbn(self):
        return self.isbn

    def get_info(self):
        return f"Book: {self.title}, Author: {self.author}, ISBN: {self.isbn}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book added: {book.get_title()}")

    def remove_book(self, isbn):
        initial_size = len(self.books)
        self.books = [book for book in self.books if book.get_isbn() != isbn]

        if len(self.books) < initial_size:
            print(f"Book with ISBN {isbn} has been removed.")
        else:
            print(f"Book with ISBN {isbn} not found.")

    def display_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(book.get_info())


def display_menu():
    print("\n -|- Library Menu -|-")
    print("1. Add book")
    print("2. Remove book by ISBN")
    print("3. Display all books")
    print("0. Exit")
    return input("Choose an option: ")


def main():
    library = Library()

    while True:
        option = display_menu()

        if option == '1':
            title = input("Enter the book title: ")
            author = input("Enter the book author: ")
            isbn = input("Enter the book ISBN: ")
            new_book = Book(title, author, isbn)
            library.add_book(new_book)

        elif option == '2':
            isbn = input("Enter the ISBN of the book to remove: ")
            library.remove_book(isbn)

        elif option == '3':
            library.display_books()

        elif option == '0':
            print("Exiting the program.")
            break

        else:
            print("Invalid option! Please choose again.")


if __name__ == "__main__":
    main()
