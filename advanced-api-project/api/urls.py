from django.urls import path
from .views import ListView, DeleteView, DetailView, CreateView,UpdateView


urlpatterns = [
    path('book/', ListView.as_view(), name='book-list'),
    path('book/detail/<int:id>', DetailView.as_view(), name='book-detail'),
    path('book/create', CreateView.as_view(), name='book-create'),
    path('book/update/<int:id>', UpdateView.as_view(), name='=book-update'),
    path('book/delete/<int:id>', DeleteView.as_view(), name='book-delete'),
]