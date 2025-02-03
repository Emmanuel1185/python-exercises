# Objective: Create a Python program that simulates a basic library system where students can borrow and return books.

# Step 1: Define the Classes
# Class: Book
# Attributes:
# title: Title of the book
# author: Author of the book
# is_available: Boolean indicating if the book is available (default: True)

class Book():
    def __init__(self,Title, Author):
        self.Title = Title
        self.Author = Author
        self.is_available = True

    def borrow(self): # If is_available is True, mark the book as borrowed and return a success message. Otherwise, return a message saying the book is already borrowed.
        if self.is_available: # Check if the book is available
            self.is_available = False # Mark the book as borrowed
            print(f" Success! {self.Title} has been borrowed") # Print a success message
        else: # If the book is not available
            print(f" Sorry, {self.Title} is already borrowed") # Print a message if the book is already borrowed

    def return_book(self):  # Mark the book as available and return a success message.
        if not self.is_available: # Check if the book is borrowed
            self.is_available = True # Mark the book as available
            print(f"{self.Title} successfully returned") # Print a success message
        else: # If the book is not borrowed
            print(f" {self.Title} was not borrowed") # Print a message if the book was not borrowed

# Class: Library
class Library():
    def __init__(self):
        self.books = []

# Methods:
    def add_book(self, book): # Add a new Book object to the library.
        self.books.append(book) # Append the book to the list of books

    def list_books(self): # List all books in the library with their availability status.
        if not self.books: # Check if the library has no books
            print("No books available in the library.") # Print a message if there are no books
        else: # If the library has books
            print("Library Books:") # Print a header for the list of books
            for book in self.books: # Iterate through each book in the library
                status = "Available" 
                if book.is_available :# Determine the status of the book
                    print(f"{book.Title} by {book.Author} ({status})") # Print the book title, author, and availability status

                else:
                    status = "Borrowed" # Determine the status of the book
                    print(f"{book.Title} by {book.Author} ({status})") # Print the book title, author, and availability status

    def find_book(self, title): # Search for a book by title and return it if found.
        for book in self.books: # Iterate through each book in the library
            if book.Title == title: # Check if the title matches the search title
                return book
        return None # Return None if the book is not found
    
    def borrow_book(self, title): # Allow a user to borrow a book by title.
        book = self.find_book(title)
        if book is not None:
            book.borrow()
        else:
            print(f"Book '{title}' not found in the library.")

    def return_book(self, title): # Allow a user to return a book by title.
        book = self.find_book(title)
        if book is not None:
            book.return_book()
        else:
            print(f"Book '{title}' not found in the library.")


# Step 2: Task Instructions
# 1. Create a list of 5 books in your library with different titles and authors.
books = {
    "A Game Of Thrones": "George R.R. Martin",
    "The Kite Runner": "Khaled Hosseini",
    "The Hobbit": "J.R.R. Tolkien",
    "Animal Farm": "George Orwell",
    "Don Quixote": "Miguel de Cervantes"
}

# 2. Use a menu system to interact with the library:

library = Library() # Create a new Library object

for title, author in books.items(): # Iterate through the books dictionary
    book = Book(title, author) # Create a new Book object
    library.add_book(book) # Add the book to the library


while True:  # Create a loop to display the menu options
        print("\nLibrary Menu:") # Display the menu options
        print("1. View all books") # Option to view all books in the library
        print("2. Borrow a book") # Option to borrow a book
        print("3. Return a book") # Option to return a book
        print("4. Exit") # Option to exit the program

        choice = input("Enter your choice: ") # Get the user's choice

        if choice == "1": # If the user chooses to view all books
            print("\nBooks in the library:")
            print(library.list_books())

        elif choice == "2": # If the user chooses to borrow a book
            title = input("Enter the title of the book to borrow: ") # Prompt the user to enter the title of the book to borrow
            print(library.borrow_book(title)) # Borrow the book

        elif choice == "3": # If the user chooses to return a book
            title = input("Enter the title of the book to return: ") #  Prompt the user to enter the title of the book to return
            print(library.return_book(title)) # Return the book

        elif choice == "4": # If the user chooses to exit the program
            print("Exiting the program. Goodbye!") #    Print a goodbye message
            break # Exit the loop

        else: # If the user enters an invalid choice
            print("Invalid choice. Please try again.") # Print an error message and prompt the user to try again

# 3. Add appropriate error handling for cases like:
# Borrowing a book that is not available.
# Returning a book that was not borrowed.
# Searching for a book that doesn't exist.


