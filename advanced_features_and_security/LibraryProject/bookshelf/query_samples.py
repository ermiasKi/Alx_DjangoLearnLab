import os
import django
import sys

# # Add the project root to Python path
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
# django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    """
    Query all books by a specific author.
    """
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        
        print(f"\nBooks by {author_name}:")
        for book in books:
            print(f"- {book.title}")
        return books
        
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found.")
        return []

def list_books_in_library(library_name):
    """
    List all books in a specific library.
    """
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        
        print(f"\nBooks in {library_name} library:")
        for book in books:
            print(f"- {book.title} by {book.author.name}")
        return books
        
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
        return []

def get_librarian_for_library(library_name):
    """
    Retrieve the librarian for a specific library.
    """
    try:
        library = Library.objects.get(name=library_name)
        
        try:
            librarian = Librarian.objects.get(library=library)
            print(f"\nLibrarian for {library_name}: {librarian.name}")
            return librarian
        except Librarian.DoesNotExist:
            print(f"No librarian found for {library_name}")
            return None
            
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
        return None

# def create_sample_data():
#     """
#     Create sample data for testing the queries.
#     """
#     # Create authors
#     author1 = Author.objects.create(name="J.K. Rowling")
#     author2 = Author.objects.create(name="George R.R. Martin")
    
#     # Create books
#     book1 = Book.objects.create(title="Harry Potter and the Philosopher's Stone", author=author1)
#     book2 = Book.objects.create(title="Harry Potter and the Chamber of Secrets", author=author1)
#     book3 = Book.objects.create(title="A Game of Thrones", author=author2)
#     book4 = Book.objects.create(title="A Clash of Kings", author=author2)
    
#     # Create libraries
#     library1 = Library.objects.create(name="Central Library")
#     library2 = Library.objects.create(name="City Library")
    
#     # Add books to libraries
#     library1.books.add(book1, book2, book3)
#     library2.books.add(book3, book4)
    
#     # Create librarians
#     Librarian.objects.create(name="Alice Johnson", library=library1)
#     Librarian.objects.create(name="Bob Smith", library=library2)
    
#     print("Sample data created successfully!")

# if __name__ == "__main__":
#     # Uncomment the line below to create sample data (run once)
#     # create_sample_data()
    
#     # Example queries
#     print("=== Relationship Query Examples ===")
    
#     # Query 1: All books by a specific author
#     query_books_by_author("J.K. Rowling")
    
#     # Query 2: All books in a library
#     list_books_in_library("Central Library")
    
#     # Query 3: Librarian for a library
#     get_librarian_for_library("Central Library")
    
#     # Additional examples
#     query_books_by_author("George R.R. Martin")
#     list_books_in_library("City Library")
#     get_librarian_for_library("City Library")