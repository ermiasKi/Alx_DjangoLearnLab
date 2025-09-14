from django import forms
from .models import Book, Author

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)