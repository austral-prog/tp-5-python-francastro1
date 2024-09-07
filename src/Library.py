from src.Book import Book
from src.User import User
from typing import List


class Library:
    def __init__(self) -> None:
        self.__books: List[Book] = []
        self.__users: List[User] = []
        self.__checked_out_books: List[Book] = []
        self.__checked_in_books: List[Book] = []

    # Getters
    def get_books(self) -> List[Book]:
        return self.__books

    def get_users(self) -> List[User]:
        return self.__users

    def get_checked_out_books(self) -> List[Book]:
        return self.__checked_out_books

    def get_checked_in_books(self) -> List[Book]:
        return self.__checked_in_books

    # 1.1 Add Book
    def add_book(self, isbn: str , title: str, author: str) -> None:
        newBook: Book = Book(isbn,title,author)
        self.__books.append(newBook)

    # 1.2 List All Books
    def list_all_books(self) -> None:
        for i in self.__books:
            print(i)

    # 2.1 Check out book
    def check_out_book(self, isbn: str, dni: int, due_date: str) -> str:
        for book in self.__books:
            if book not in self.__checked_out_books:
                book.set_available(False)
                self.__checked_out_books.append(book)
                return f"User {dni} checked out book {isbn}"
            return f'Book {isbn} is not available'

    # 2.2 Check in book
    def check_in_book(self, isbn: str, dni: int, returned_date: str) -> str:
        for book in self.__books:
            if book not in self.__checked_in_books:
                book.set_available(True)
                self.__checked_in_books.append(book)
                for i in range(len(self.__checked_out_books)):
                    if self.__checked_out_books[i] == book:
                        del self.__checked_out_books[i]
                return f"Book {isbn} checked in by user {dni}"

    # Utils
    def add_user(self, dni: int, name: str) -> None:
        newUser: User = User(dni, name)
        self.__users.append(newUser)
