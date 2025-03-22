# booklover_test.py

import unittest
from booklover import BookLover
import warnings
warnings.filterwarnings("ignore")

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self):
        """Test adding a book and checking if it's in book_list."""
        bl = BookLover("Alice", "alice@example.com", "Fantasy")
        bl.add_book("The Hobbit", 5)
        self.assertTrue("The Hobbit" in bl.book_list['book_name'].values)

    def test_2_add_book(self):
        """Test adding the same book twice and ensure it's only in book_list once."""
        bl = BookLover("Alice", "alice@example.com", "Fantasy")
        bl.add_book("The Hobbit", 5)
        bl.add_book("The Hobbit", 5)
        self.assertEqual(len(bl.book_list[bl.book_list['book_name'] == "The Hobbit"]), 1)

    def test_3_has_read(self):
        """Test if a book in the list returns True."""
        bl = BookLover("Alice", "alice@example.com", "Fantasy")
        bl.add_book("The Hobbit", 5)
        self.assertTrue(bl.has_read("The Hobbit"))

    def test_4_has_read(self):
        """Test if a book NOT in the list returns False."""
        bl = BookLover("Alice", "alice@example.com", "Fantasy")
        self.assertFalse(bl.has_read("The Catcher in the Rye"))

    def test_5_num_books_read(self):
        """Test if num_books_read() returns the correct number."""
        bl = BookLover("Alice", "alice@example.com", "Fantasy")
        bl.add_book("The Hobbit", 5)
        bl.add_book("Harry Potter", 4)
        self.assertEqual(bl.num_books_read(), 2)

    def test_6_fav_books(self):
        """Test if fav_books() returns only books with rating > 3."""
        bl = BookLover("Alice", "alice@example.com", "Fantasy")
        bl.add_book("The Hobbit", 5)
        bl.add_book("Harry Potter", 4)
        bl.add_book("Twilight", 2)
        
        fav_books = bl.fav_books()
        self.assertTrue(all(fav_books['book_rating'] > 3))

if __name__ == '__main__':
    unittest.main(verbosity=3)