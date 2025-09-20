# Create a Book instance
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)

book

### expected outcome
<Book: 1984 by George Orwell (1949)>
