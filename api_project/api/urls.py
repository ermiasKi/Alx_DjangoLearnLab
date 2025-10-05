<<<<<<< HEAD
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from django.urls import path, include
from .views import BookList
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token.as_view(), name='api-token-auth')
=======
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from django.urls import path, include
from .views import BookList
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token.as_view(), name='api-token-auth')
>>>>>>> 9102b10 (blog apps)
]