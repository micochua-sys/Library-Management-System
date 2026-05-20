"""
Main entry point for the Library Management System.
Provides interactive menu for library operations.
"""

from library_service import LibraryService
from exceptions.custom_exceptions import (
    BookNotFoundError,
    MemberNotFoundError,
    BookUnavailableError,
    LoanNotFoundError
)


def print_menu():
    """Display the main menu."""
    print("\n" + "=" * 50)
    print("        LIBRARY MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Add Book")
    print("2. Register Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. View Books")
    print("6. View Members")
    print("7. View Loans")
    print("8. Exit")
    print("=" * 50)


def add_book(service):
    """Handle adding a new book to the library."""
    print("\n--- Add Book ---")
    try:
        book_id = input("Enter Book ID: ").strip()
        title = input("Enter Book Title: ").strip()
        author = input("Enter Book Author: ").strip()
        
        if not book_id or not title or not author:
            print("❌ Error: All fields are required.")
            return
        
        book = service.add_book(book_id, title, author)
        print(f"✓ Book added successfully: {book}")
    except Exception as e:
        print(f"❌ Error: {str(e)}")


def register_member(service):
    """Handle registering a new member."""
    print("\n--- Register Member ---")
    try:
        member_id = input("Enter Member ID: ").strip()
        name = input("Enter Member Name: ").strip()
        email = input("Enter Member Email: ").strip()
        
        if not member_id or not name or not email:
            print("❌ Error: All fields are required.")
            return
        
        member = service.register_member(member_id, name, email)
        print(f"✓ Member registered successfully: {member}")
    except Exception as e:
        print(f"❌ Error: {str(e)}")


def borrow_book(service):
    """Handle borrowing a book."""
    print("\n--- Borrow Book ---")
    try:
        book_id = input("Enter Book ID: ").strip()
        member_id = input("Enter Member ID: ").strip()
        
        if not book_id or not member_id:
            print("❌ Error: All fields are required.")
            return
        
        loan = service.borrow_book(book_id, member_id)
        print(f"✓ Book borrowed successfully!")
        print(f"  Loan ID: {loan.loan_id}")
        print(f"  Member: {loan.member.name}")
        print(f"  Book: {loan.book.title}")
        print(f"  Borrow Date: {loan.borrow_date.strftime('%Y-%m-%d %H:%M:%S')}")
    except (BookNotFoundError, MemberNotFoundError, BookUnavailableError) as e:
        print(f"❌ Error: {str(e)}")
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")


def return_book(service):
    """Handle returning a book."""
    print("\n--- Return Book ---")
    try:
        loan_id = input("Enter Loan ID: ").strip()
        
        if not loan_id:
            print("❌ Error: Loan ID is required.")
            return
        
        loan = service.return_book(loan_id)
        print(f"✓ Book returned successfully!")
        print(f"  Loan ID: {loan.loan_id}")
        print(f"  Member: {loan.member.name}")
        print(f"  Book: {loan.book.title}")
        print(f"  Return Date: {loan.return_date.strftime('%Y-%m-%d %H:%M:%S')}")
    except LoanNotFoundError as e:
        print(f"❌ Error: {str(e)}")
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")


def view_books(service):
    """Display all books in the library."""
    print("\n--- View Books ---")
    books = service.view_books()
    if not books:
        print("No books found.")
    else:
        print(f"\nTotal books: {len(books)}\n")
        for book in books:
            print(f"  {book}")


def view_members(service):
    """Display all registered members."""
    print("\n--- View Members ---")
    members = service.view_members()
    if not members:
        print("No members found.")
    else:
        print(f"\nTotal members: {len(members)}\n")
        for member in members:
            print(f"  {member}")


def view_loans(service):
    """Display all loan transactions."""
    print("\n--- View Loans ---")
    loans = service.view_loans()
    if not loans:
        print("No loans found.")
    else:
        print(f"\nTotal loans: {len(loans)}\n")
        for loan in loans:
            print(f"  {loan}")


def main():
    """Main program loop."""
    service = LibraryService()
    
    print("\n" + "=" * 50)
    print("   Welcome to Library Management System")
    print("=" * 50)
    
    while True:
        print_menu()
        choice = input("Enter your choice (1-8): ").strip()
        
        if choice == "1":
            add_book(service)
        elif choice == "2":
            register_member(service)
        elif choice == "3":
            borrow_book(service)
        elif choice == "4":
            return_book(service)
        elif choice == "5":
            view_books(service)
        elif choice == "6":
            view_members(service)
        elif choice == "7":
            view_loans(service)
        elif choice == "8":
            print("\n✓ Program closed. Thank you for using Library Management System!")
            break
        else:
            print("❌ Invalid choice. Please select an option between 1 and 8.")


if __name__ == "__main__":
    main()
