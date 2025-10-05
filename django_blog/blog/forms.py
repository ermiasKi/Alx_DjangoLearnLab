from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Post, Comment
from taggit.forms import TagWidget

User = get_user_model()

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)


class PostForm(forms.ModelForm):
    tags = forms.CharField(
        required=False,
        widget = TagWidget(attrs={'class':'form-tag', 'placeholder':'Enter tags separated by commas' }),
        help_text='Separate tags with commas'
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
    
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 5:
            raise forms.ValidationError("Title must be at least 5 characters long")
        return title
    
    def clean_content(self):
        content = self.cleaned_data['content']
        if len(content) < 10:
            raise forms.ValidationError("Content must be at least 10 characters long")
        return content


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 3, 
                'placeholder': 'Write your comment here...'
            }),
        }

    def clean_content(self):
        content = self.cleaned_data['content']

        if not content:
            raise forms.ValidationError("This field cann't be empty")
        return content
