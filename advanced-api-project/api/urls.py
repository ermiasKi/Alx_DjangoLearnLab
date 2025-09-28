from django.urls import path
from .views import ListView, DeleteView, DetailView, CreateView,UpdateView


urlpatterns = [
    path('book/list', ListView.as_view(), name='book-list'),
    path('book/retrieve/<int:id>', DetailView.as_view(), name='book-detail'),
    path('book/add', CreateView.as_view(), name='book-create'),
    path('book/modify/<int:id>', UpdateView.as_view(), name='=book-update'),
    path('book/remove/<int:id>', DeleteView.as_view(), name='book-delete'),
]