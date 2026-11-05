class Book:
    def __init__(self, title="Untitled", author="Unknown"):
        self.title = title
        self.author = author
        self.checkout_count = 0
        print(f"Book created: '{self.title}' by {self.author}")

    def checkout(self):
        self.checkout_count += 1
        print(f"'{self.title}' checked out (Total: {self.checkout_count})")

    def __del__(self):
        print(f"Book destroyed: '{self.title}' had {self.checkout_count} checkouts")


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        print(f"Library '{self.name}' created")

    def add_book(self, book):
        self.books.append(book)
        print(f"Added '{book.title}' to {self.name}")

    def __del__(self):
        print(f"Library '{self.name}' destroyed with {len(self.books)} books")


def demonstrate_lifecycle():
    print("\n=== OBJECT LIFECYCLE DEMONSTRATION ===")
    book1 = Book("Python Programming", "A. Writer")
    book2 = Book("Clean Code", "Robert C. Martin")

    main_library = Library("Central Library")
    main_library.add_book(book1)
    main_library.add_book(book2)

    book1.checkout()
    book1.checkout()
    book2.checkout()

    print("\n=== LEAVING THE DEMONSTRATION FUNCTION ===")


if __name__ == "__main__":
    print("=== CONSTRUCTORS AND DESTRUCTORS DEMONSTRATION ===")
    temp_obj = Book()
    del temp_obj
    demonstrate_lifecycle()
    print("\n=== END OF DEMONSTRATION ===")
