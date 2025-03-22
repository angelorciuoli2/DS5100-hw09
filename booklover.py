# booklover.py

import pandas as pd
import warnings
warnings.filterwarnings("ignore")

class BookLover:
    def __init__(self, name, email, fav_genre, num_books=0, book_list=None):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})

    def add_book(self, book_name, rating):
        """Adds a book to the book list if it's not already there."""
        if book_name in self.book_list['book_name'].values:
            print(f"{book_name} is already in the book list.")
            return
        
        new_book = pd.DataFrame({
            'book_name': [book_name],
            'book_rating': [rating]
        })
        
        self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
        self.num_books += 1  # Book count

    def has_read(self, book_name):
        """Checks if the book has been read."""
        return book_name in self.book_list['book_name'].values

    def num_books_read(self):
        """Returns the total number of books read."""
        return self.num_books

    def fav_books(self):
        """Returns a DataFrame of favorite books (rating > 3)."""
        return self.book_list[self.book_list['book_rating'] > 3]
    
if __name__ == '__main__':

    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_book("War of the Worlds", 4)