from booklover.booklover import BookLover

# Create a BookLover instance
bl = BookLover("Alice", "alice@example.com", "Fantasy")

# Add books
bl.add_book("The Hobbit", 5)
bl.add_book("Harry Potter", 4)
bl.add_book("Twilight", 2)

# Check if books were added
print(bl.book_list)

# Test the `has_read` method
print(f"Has Alice read 'The Hobbit'? {bl.has_read('The Hobbit')}")  # Should print True
print(f"Has Alice read 'The Catcher in the Rye'? {bl.has_read('The Catcher in the Rye')}")  # Should print False

# Test the `num_books_read` method
print(f"Number of books read by Alice: {bl.num_books_read()}")  # Should print 3

# Test the `fav_books` method
fav_books = bl.fav_books()
print(f"Favorite books (rating > 3):")
print(fav_books)

