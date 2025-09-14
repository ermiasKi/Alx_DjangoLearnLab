from django.urls import path
from django.contrib.auth import views as auth_views
import views

urlspattern = [
    path("list/", views.query_books_by_author),
    path('library/', views.LibraryDetailView.as_view()),
    path('register/', auth_views.RegisterView.as_view(template_name='relationship_app/register.html'), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path("admin/", views.Admin),
    path("member/", views.Member),
    path("librarian/", views.Librarian),
    path('books/add/', views.add_book, name='add_book'),
    path('books/edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('books/delete/<int:book_id>/', views.delete_book, name='delete_book'),
]