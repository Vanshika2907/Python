
# To develop a library management system using classes and objects to manage books and their availability.
class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append({
            "title": book,
            "available": True
        })
        print("Book added successfully!")

    def display_books(self):
        print("\nLibrary Books:")

        if not self.books:
            print("No books available.")
            return

        for book in self.books:
            status = "Available" if book["available"] else "Issued"
            print(book["title"], "-", status)

    def issue_book(self, book_name):
        for book in self.books:
            if book["title"].lower() == book_name.lower():
                if book["available"]:
                    book["available"] = False
                    print("Book issued successfully!")
                else:
                    print("Book is already issued!")
                return

        print("Book not found!")

    def return_book(self, book_name):
        for book in self.books:
            if book["title"].lower() == book_name.lower():
                if not book["available"]:
                    book["available"] = True
                    print("Book returned successfully!")
                else:
                    print("Book was not issued!")
                return

        print("Book not found!")


library = Library()

while True:
    print("\n1. Add Book")
    print("2. Display Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Book Name: ")
        library.add_book(name)

    elif choice == "2":
        library.display_books()

    elif choice == "3":
        name = input("Enter Book Name to Issue: ")
        library.issue_book(name)

    elif choice == "4":
        name = input("Enter Book Name to Return: ")
        library.return_book(name)

    elif choice == "5":
        print("Exiting Library System.")
        break

    else:
        print("Invalid choice!")
