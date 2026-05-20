# Library Management System

A Python-based library management system with features for managing books, members, and loans.

## Features

### 1. Add Book
- Add new books to the library inventory
- Store book ID, title, and author
- Books are available by default

### 2. Register Member
- Register new library members
- Store member ID, name, and email

### 3. Borrow Book
- Members can borrow available books
- Validates book and member existence
- Tracks loan with unique loan ID
- Sets book as unavailable
- Error handling for:
  - Book not found
  - Member not found
  - Book already borrowed

### 4. Return Book
- Members can return borrowed books
- Closes the loan transaction
- Sets book as available again
- Calculates return date

### 5. View Books
- Display all books in the library
- Shows availability status (Available/Borrowed)
- Lists: Book ID, Title, Author, Status

### 6. View Members
- Display all registered members
- Shows: Member ID, Name, Email

### 7. View Loans
- Display all loan transactions
- Shows: Loan ID, Member Name, Book Title, Status (Active/Closed)

### 8. Exit
- Gracefully close the program

## Project Structure

```
Library-Management-System/
├── main.py                          # Entry point with menu system
├── library_service.py               # Core business logic
├── models/
│   ├── __init__.py
│   ├── book.py                      # Book class
│   ├── member.py                    # Member class
│   └── loan.py                      # Loan class
├── exceptions/
│   └── custom_exceptions.py         # Custom exception classes
└── README.md                        # This file
```

## Installation

```bash
git clone https://github.com/micochua-sys/Library-Management-System.git
cd Library-Management-System
```

## Usage

```bash
python main.py
```

The program will display an interactive menu with 8 options.

## Exception Handling

- **BookNotFoundError**: Raised when a book ID doesn't exist
- **MemberNotFoundError**: Raised when a member ID doesn't exist
- **BookUnavailableError**: Raised when attempting to borrow an already borrowed book
- **LoanNotFoundError**: Raised when a loan ID doesn't exist

## Data Structures

### Book
- `book_id`: Unique identifier
- `title`: Book title
- `author`: Book author
- `available`: Boolean (True/False)

### Member
- `member_id`: Unique identifier
- `name`: Member name
- `email`: Member email

### Loan
- `loan_id`: Unique identifier (L001, L002, ...)
- `book`: Book object
- `member`: Member object
- `borrow_date`: Timestamp when borrowed
- `return_date`: Timestamp when returned (None if active)
- `is_active`: Boolean status
