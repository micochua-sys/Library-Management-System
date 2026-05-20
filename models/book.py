"""Book model for Library Management System."""


class Book:
    """Represents a book in the library."""
    
    def __init__(self, book_id, title, author):
        """Initialize a Book object.
        
        Args:
            book_id: Unique identifier for the book
            title: Title of the book
            author: Author of the book
        """
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True  # Books are available by default
    
    def borrow(self):
        """Mark the book as borrowed."""
        self.available = False
    
    def return_book(self):
        """Mark the book as available."""
        self.available = True
    
    def __str__(self):
        """String representation of the book."""
        status = "Available" if self.available else "Borrowed"
        return f"{self.book_id} - {self.title} by {self.author} [{status}]"
    
    def __repr__(self):
        """Developer representation of the book."""
        return f"Book(id={self.book_id}, title={self.title}, author={self.author}, available={self.available})"
