<<<<<<< HEAD
from django.urls import path
from django.contrib.auth import views as auth_views
import relationship_app.views as views
from .views import list_books

urlspattern = [
    path("list/", views.list_books),
    path('library/', views.LibraryDetailView.as_view()),
    path('register/', views.register.as_view(template_name='relationship_app/register.html'), name='register'),
    path('login/', views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path("admin/", views.Admin),
    path("member/", views.Member),
    path("librarian/", views.Librarian),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
=======
from django.urls import path
from django.contrib.auth import views as auth_views
import relationship_app.views as views
from .views import list_books

urlspattern = [
    path("list/", views.list_books),
    path('library/', views.LibraryDetailView.as_view()),
    path('register/', views.register.as_view(template_name='relationship_app/register.html'), name='register'),
    path('login/', views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path("admin/", views.Admin),
    path("member/", views.Member),
    path("librarian/", views.Librarian),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
>>>>>>> 9102b10 (blog apps)
]