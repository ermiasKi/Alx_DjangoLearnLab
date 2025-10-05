from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, logout, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Post, Comment
from .forms import PostForm, CommentForm

User = get_user_model()

# Create your views here.

from django.middleware.csrf import get_token

def get_csrf_token(request):
    """View to get CSRF token for Postman testing"""
    return JsonResponse({'csrfToken': get_token(request)})

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        errors = []
        # MANUAL VALIDATION

        # check if username exists
        if User.objects.filter(username=username).exists():
            errors.append("User Already Exists")

        if not errors:
            user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
        )
            messages.success(request, "User Created Successfully, please login.")
            
            return redirect('login')
        
        else:
            for error in errors:
                messages.error(request, error)
            return render(request, 'register.html', {
                'username': username,
                'email': email,
                'first_name': first_name,
                'last_name': last_name,
            })
        
        
    return render(request, 'register.html')


def UserLogin(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        
        if user is not None:
            login(request, user)
            messages.success(request, f"wellcome {username}")
            return redirect('home')
        else:
            messages.error(request, "invalid username or password")
            return render(request, 'login.html')

@login_required
def profile(request):
    if request.method == 'POST':
        user = request.user
        user.email = request.POST.get('email', user.email)
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.save()

        messages.success(request, "Profile updated successfully")
        return redirect('profile')
    return render(request, 'profile.html')


def UserLogout(request):
    logout(request)
    messages.success(request, "you have been logged out successfully")
    return render(request, 'home.html')

    
def home(request):
    return render(request, 'home.html')


class PostListView(ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = 'post_list.html'
    context_object_name = 'posts'
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
    


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'post_form.html'
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'post_form.html'
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        # Only allow the author to edit the post
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('post-list')
    
    def test_func(self):
        post = self.get_object()
        # Only allow the author to delete the post
        return self.request.user == post.author
    

class CommentListView(ListView):
    model = Comment
    context_object_name = 'comments'
    template_name = 'comments_list.html'
    paginate_by = 20


class CommentDetailView(DetailView):
    model = Comment
    context_object_name = 'comment'
    template_name = 'comment_list.html'


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs['post_id']

        response = super().form_valid(form)
        messages.success(self.request, "Comment added successfully")
        return response
    
    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk':self.kwargs['post_id']})


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment_update.html'

    # used by UserPassTestMixin
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author
    
    # used by the generic views to validate the form
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    # used fro redirecting
    def get_success_url(self):
        return redirect('post-detail', kwargs={'pk':self.object.post.pk})

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'comment_delete.html'

    def test_func(self):
        return self.request.user == self.get_object().author
    
    def get_success_url(self):
        # Remember the post before deleting
        post_pk = self.object.post.pk
        messages.success(self.request, 'Comment deleted successfully!')
        return reverse_lazy('post-detail', kwargs={'pk': post_pk})