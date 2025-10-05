from django.urls import path
from . import views


urlpatterns = [
    # user
    path('login/', views.UserLogin, name='login'),
    path('logout/', views.UserLogout, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('', views.home, name='home'),

    # post
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

    # comment
    path('comments/', views.CommentListView.as_view(), name='comment-list'),
    path('posts/<int:post_id>/comments/<int:pk>/', views.CommentDetailView.as_view(), name='comment-detail'),
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment-create'),
    path('posts/<int:post_id>/comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment-update'),
    path('posts/<int:post_id>/comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),

    # csrf
    path('get-csrf-token/', views.get_csrf_token, name='get-csrf-token'),

    # tag
    path('tags/<slug:tag_slug>/', views.PostByTagListView.as_view()),
]