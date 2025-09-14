from django.urls import path
import views

urlspattern = [
    path("list/", views.query_books_by_author),
    path('library/', views.LibraryDetailView.as_view()),
    path("login/", views.login),
    path("logout/", views.logout),
    path("register/", views.register),
    path("admin/", views.admin_view),
    path("member/", views.member_view),
    path("librarian/", views.librarian_view),
    path('books/add/', views.add_book, name='add_book'),
    path('books/edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('books/delete/<int:book_id>/', views.delete_book, name='delete_book'),
]