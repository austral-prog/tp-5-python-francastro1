import io
import unittest.mock

from src.Book import Book
from src.Library import Library


class LibraryTests(unittest.TestCase):
    def setUp(self):
        self.library = Library()

    def test_add_book(self):
        self.library.add_book("9780743273565", "The Great Gatsby", "Fitzgerald")
        assert len(self.library.get_books()) == 1
        first_book = self.library.get_books()[0]
        compare_book = Book("9780743273565", "The Great Gatsby", "Fitzgerald", True, 0)
        self.assertEqual(first_book, compare_book, "Books with the same ISBN should be equal")

        self.library.add_book("9780743273566", "The Great Gatsby 2", "Fitzgerald")
        assert len(self.library.get_books()) == 2
        second_book = self.library.get_books()[1]
        compare_book = Book("9780743273566", "The Great Gatsby 2", "Fitzgerald", True, 0)
        self.assertEqual(second_book, compare_book, "Books with the same ISBN should be equal")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_list_all_books(self, mock_stdout):
        self.library.add_book("9780451524935","1984", "Orwell")
        self.library.add_book("9780061120084", "To Kill a Mockingbird", "Lee")
        self.library.list_all_books()

        results = mock_stdout.getvalue().splitlines()

        self.assertEqual(results[0], "ISBN: 9780451524935, Title: 1984, Author: Orwell")
        self.assertEqual(results[1], "ISBN: 9780061120084, Title: To Kill a Mockingbird, Author: Lee")


    def test_check_out_book(self):
        self.library.add_book("9781503280786", "Moby Dick", "Melville")
        self.library.add_user(11111111, "John Doe")

        assert self.library.check_out_book("9781503280786", 11111111, "10/09/2024") == "User 11111111 checked out book 9781503280786"
        assert self.library.get_books()[0].is_available() == False  # The book should now be unavailable
        assert len(self.library.get_checked_out_books()) == 1


    def test_check_out_unavailable_book(self):
        self.library.add_book("9781503280786", "Moby Dick", "Melville")
        self.library.add_user(11111111, "John Doe")
        self.library.check_out_book("9781503280786", 11111111, "10/09/2024")

        # Try to check out the same book again
        assert self.library.check_out_book("9781503280786", 11111111, "11/09/2024") == "Book 9781503280786 is not available"


    def test_return_book(self):
        self.library.add_book("9781503280786", "Moby Dick", "Melville")
        self.library.add_user(11111111, "John Doe")
        self.library.check_out_book("9781503280786", 11111111, "10/09/2024")

        assert self.library.check_in_book("9781503280786", 11111111, "15/09/2024") == "Book 9781503280786 checked in by user 11111111"
        assert self.library.get_books()[0].is_available() == True  # The book should now be available again
        assert len(self.library.get_checked_out_books()) == 0
        assert len(self.library.get_checked_in_books()) == 1

