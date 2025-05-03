class Book:
    total_books = 0 

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1  

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count() 

book1 = Book("Book Title 1", "Author 1")
book2 = Book("Book Title 2", "Author 2")

print("Total books:", Book.total_books)

