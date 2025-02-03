
class Book:
    def __init__(self, Title, Author, is_available=True):
        self.Title = Title
        self.Author = Author
        self.is_available = is_available

    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f" Success! {self.Title} has been borrowed")
        else:
            print(f" Sorry, {self.Title} is already borrowed")      
    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(f"{self.Title} successfully returned")
        else:
            print(f" {self.Title} was not borrowed")
    def __str__(self):
        return f"{self.Title} by {self.Author}"
    
class Library:
    def __init__(self, books=[]):
        self.books = books
       
    def add_book(self, book):
        self.books.append(book)
    
    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books:
                status = "Available" if book.is_available else "Borrowed"
                print(f"{book} ({status})")
        else:
            print("No books available in the library.")

    def find_book(self, title):
        for book in self.books:
            if book.Title == title:
                return book
        return None
    
    def borrow_book(self, title):
        book = self.find_book(title)
        if book is not None:
            book.borrow()
        else:
            print(f"Book '{title}' not found in the library.")
    def return_book(self, title):
        book = self.find_book(title)
        if book is not None:
            book.return_book()
        else:
            print(f"Book '{title}' not found in the library.")
    
# Main program

# Create a new Library object
library = Library()

# Create a list of books
books = [("The Great Gatsby", "F. Scott Fitzgerald"), 
         ("To Kill a Mockingbird", "Harper Lee"), 
         ("1984", "George Orwell")]

# Add the books to the library
for title, author in books:
    library.add_book(Book(title, author))

# Display the Library menu
while True:
    choice = input("\nLibrary Menu:\n1. View all books\n2. Borrow a book\n3. Return a book\n4. Exit\nEnter your choice: ")
    if choice == "1":
        library.list_books()
    elif choice == "2":
        library.borrow_book(input("Enter the title of the book to borrow: "))
    elif choice == "3":
        library.return_book(input("Enter the title of the book to return: "))
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
