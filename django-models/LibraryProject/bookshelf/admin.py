<<<<<<< HEAD
from django.contrib import admin
from .models import Book

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title','author','publication_year']
    list_filter = ['title', 'author']
    search_fields = ['title__icontains','author__icontains']

=======
from django.contrib import admin
from .models import Book

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title','author','publication_year']
    list_filter = ['title', 'author']
    search_fields = ['title__icontains','author__icontains']

>>>>>>> 9102b10 (blog apps)
