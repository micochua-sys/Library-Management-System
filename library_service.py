"""LibraryService class for managing library operations."""

from models.book import Book
from models.member import Member
from models.loan import Loan
from exceptions.custom_exceptions import (
    BookNotFoundError,
    MemberNotFoundError,
    BookUnavailableError,
    LoanNotFoundError
)


class LibraryService:
    """Service class for library management operations."""
    
    def __init__(self):
        """Initialize the LibraryService with empty data structures."""
        self._books = {}        # Dictionary: book_id -> Book
        self._members = {}      # Dictionary: member_id -> Member
        self._loans = []        # List of Loan objects
        self._loan_counter = 0  # Counter for generating loan IDs
    
    def add_book(self, book_id, title, author):
        """Add a new book to the library.
        
        Args:
            book_id: Unique identifier for the book
            title: Title of the book
            author: Author of the book
            
        Returns:
            Book: The newly created book object
        """
        book = Book(book_id, title, author)
        self._books[book_id] = book
        return book
    
    def register_member(self, member_id, name, email):
        """Register a new library member.
        
        Args:
            member_id: Unique identifier for the member
            name: Name of the member
            email: Email address of the member
            
        Returns:
            Member: The newly created member object
        """
        member = Member(member_id, name, email)
        self._members[member_id] = member
        return member
    
    def borrow_book(self, book_id, member_id):
        """Process a book borrowing request.
        
        Args:
            book_id: ID of the book to borrow
            member_id: ID of the member borrowing
            
        Returns:
            Loan: The created loan object
            
        Raises:
            BookNotFoundError: If book doesn't exist
            MemberNotFoundError: If member doesn't exist
            BookUnavailableError: If book is already borrowed
        """
        # Check if book exists
        book = self._books.get(book_id)
        if book is None:
            raise BookNotFoundError(f"Book not found: {book_id}")
        
        # Check if member exists
        member = self._members.get(member_id)
        if member is None:
            raise MemberNotFoundError(f"Member not found: {member_id}")
        
        # Check if book is available
        if not book.available:
            raise BookUnavailableError(f"Book is already borrowed: {book.title}")
        
        # Mark book as borrowed
        book.borrow()
        
        # Create and store loan
        self._loan_counter += 1
        loan_id = f"L{self._loan_counter:03d}"
        loan = Loan(loan_id, book, member)
        self._loans.append(loan)
        
        return loan
    
    def return_book(self, loan_id):
        """Process a book return request.
        
        Args:
            loan_id: ID of the loan to close
            
        Returns:
            Loan: The closed loan object
            
        Raises:
            LoanNotFoundError: If loan doesn't exist
        """
        # Find the loan
        loan = None
        for l in self._loans:
            if l.loan_id == loan_id:
                loan = l
                break
        
        if loan is None:
            raise LoanNotFoundError(f"Loan not found: {loan_id}")
        
        # Return the book
        loan.book.return_book()
        
        # Close the loan
        loan.close_loan()
        
        return loan
    
    def view_books(self):
        """Get a list of all books in the library.
        
        Returns:
            list: List of Book objects
        """
        return list(self._books.values())
    
    def view_members(self):
        """Get a list of all registered members.
        
        Returns:
            list: List of Member objects
        """
        return list(self._members.values())
    
    def view_loans(self):
        """Get a list of all loan transactions.
        
        Returns:
            list: List of Loan objects
        """
        return self._loans
