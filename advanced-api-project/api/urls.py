from django.urls import path
from .views import ListView, DeleteView, DetailView, CreateView,UpdateView


urlpatterns = [
    path('books/', ListView.as_view(), name='book-list'),
    path('books/detail/<int:id>', DetailView.as_view(), name='book-detail'),
    path('books/create', CreateView.as_view(), name='book-create'),
    path('books/update/<int:id>', UpdateView.as_view(), name='=book-update'),
    path('books/delete/<int:id>', DeleteView.as_view(), name='book-delete'),
]