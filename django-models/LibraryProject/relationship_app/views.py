from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test, login_required, permission_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import BookForm
# Create your views here.

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    """
    View to add a new book (requires can_add_book permission)
    """
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to book list after success
    else:
        form = BookForm()
    
    return render(request, 'relationship_app/add_book.html', {'form': form})

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    """
    View to edit an existing book (requires can_change_book permission)
    """
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to book list after success
    else:
        form = BookForm(instance=book)
    
    return render(request, 'relationship_app/edit_book.html', {'form': form, 'book': book})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    """
    View to delete a book (requires can_delete_book permission)
    """
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  # Redirect to book list after deletion
    
    return render(request, 'relationship_app/delete_book.html', {'book': book})



def query_books_by_author(request):
    """
    Query all books by a specific author.
    """
    books = Book.objects.all()
    return render(request, 'list_books.html', {"books":books})

class LibraryDetailView(DetailView):
    """
    Class-based view to display details for a specific library
    and list all books available in that library.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
    def get_context_data(self, **kwargs):
        """
        Add additional context data - all books in the library
        """
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['books'] = library.books.all().select_related('author')
        return context
    
def register(request):
    form = UserCreationForm(request.POST)  # get the form from the request object
    if form.is_valid():
        user = form.save()      # saving the user ( registering the user data into our database )

        return redirect('relationship_app:login')


def login(request):
    form = AuthenticationForm(request, data=request.POST)  # get the data from the login form

    if form.is_valid(): # check if the form is valid
        username = form.cleaned_data.get('username')     # get the username and password ( we can get the password or other credential as well)
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)   # authenticate if the given username's password is correct

    if user is not None:   # if the user credentails are valid login the user
            login(request, user)
            return redirect('relationship_app:list_books')


def logout(request):
    logout(request)
    return render(request, 'logout.html')


# Utility functions for role checking
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# Role-based views
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')