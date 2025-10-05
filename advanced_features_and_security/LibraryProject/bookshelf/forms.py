<<<<<<< HEAD
from django import forms
from django.core.exceptions import ValidationError
from .models import Book

class ExampleForm(forms.Form):
    """
    Example form for demonstration purposes.
    Includes various field types and custom validation.
    """
    title = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter book title'
        }),
        help_text="Enter the title of the book"
    )
    
    author = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter author name'
        })
    )
    
    publication_year = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Publication year'
        }),
        min_value=1000,
        max_value=2030
    )
    
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Book description'
        })
    )
    
    is_available = forms.BooleanField(
        required=False,
        initial=True,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'
        })
    )
    
    def clean_publication_year(self):
        """Custom validation for publication year"""
        year = self.cleaned_data.get('publication_year')
        if year and year < 1000:
            raise ValidationError("Publication year must be 1000 or later.")
        return year
    
    def clean(self):
        """Form-wide validation"""
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        author = cleaned_data.get('author')
        
        # Check if book with same title and author already exists
        if title and author:
            if Book.objects.filter(title=title, author=author).exists():
                raise ValidationError(
                    "A book with this title and author already exists."
                )
        
        return cleaned_data


class BookForm(forms.ModelForm):
    """Form for creating and updating Book model instances"""
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year', 'description', 'is_available', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'publication_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'is_available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }
    
    def clean_publication_year(self):
        year = self.cleaned_data.get('publication_year')
        if year and (year < 1000 or year > 2030):
            raise ValidationError("Publication year must be between 1000 and 2030.")
=======
from django import forms
from django.core.exceptions import ValidationError
from .models import Book

class ExampleForm(forms.Form):
    """
    Example form for demonstration purposes.
    Includes various field types and custom validation.
    """
    title = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter book title'
        }),
        help_text="Enter the title of the book"
    )
    
    author = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter author name'
        })
    )
    
    publication_year = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Publication year'
        }),
        min_value=1000,
        max_value=2030
    )
    
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Book description'
        })
    )
    
    is_available = forms.BooleanField(
        required=False,
        initial=True,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'
        })
    )
    
    def clean_publication_year(self):
        """Custom validation for publication year"""
        year = self.cleaned_data.get('publication_year')
        if year and year < 1000:
            raise ValidationError("Publication year must be 1000 or later.")
        return year
    
    def clean(self):
        """Form-wide validation"""
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        author = cleaned_data.get('author')
        
        # Check if book with same title and author already exists
        if title and author:
            if Book.objects.filter(title=title, author=author).exists():
                raise ValidationError(
                    "A book with this title and author already exists."
                )
        
        return cleaned_data


class BookForm(forms.ModelForm):
    """Form for creating and updating Book model instances"""
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year', 'description', 'is_available', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'publication_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'is_available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }
    
    def clean_publication_year(self):
        year = self.cleaned_data.get('publication_year')
        if year and (year < 1000 or year > 2030):
            raise ValidationError("Publication year must be between 1000 and 2030.")
>>>>>>> 9102b10 (blog apps)
        return year