# save this as create_mock_data.py in your blog app, then run: python manage.py shell < blog/create_mock_data.py

from django.contrib.auth.models import User
from blog.models import Post, Comment

def create_mock_data():
    # Delete existing data (optional)
    Comment.objects.all().delete()
    Post.objects.all().delete()
    User.objects.exclude(username__in=['admin', 'your_username']).delete()

    # Create users
    users = []
    user_data = [
        ('john_doe', 'john@example.com', 'John', 'Doe'),
        ('jane_smith', 'jane@example.com', 'Jane', 'Smith'),
        ('bob_wilson', 'bob@example.com', 'Bob', 'Wilson'),
        ('alice_brown', 'alice@example.com', 'Alice', 'Brown'),
    ]
    
    for username, email, first_name, last_name in user_data:
        user = User.objects.create_user(username, email, 'password123')
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        users.append(user)
    
    # Create posts
    posts = []
    post_data = [
        ('Getting Started with Django', 
         'Django is a high-level Python web framework that enables rapid development...', users[0]),
        ('Understanding Django Models', 
         'Models in Django are a single, definitive source of information about your data...', users[1]),
        ('Django Templates and Views', 
         'Django template system allows you to define the outer layer of your application...', users[0]),
        ('Building REST APIs with Django REST Framework', 
         'Django REST framework is a powerful and flexible toolkit for building Web APIs...', users[2]),
        ('Django Authentication System', 
         'Django comes with a user authentication system. It handles user accounts, groups...', users[1]),
    ]
    
    for title, content, author in post_data:
        post = Post.objects.create(title=title, content=content, author=author)
        posts.append(post)
    
    # Create comments
    comment_data = [
        (posts[0], users[1], 'Great introduction to Django! Looking forward to more tutorials.'),
        (posts[0], users[2], 'This was really helpful for getting started. Could you cover deployment options?'),
        (posts[0], users[3], 'Nice overview! I especially liked the security features section.'),
        (posts[1], users[0], 'Models are indeed the foundation of any Django application. Well explained!'),
        (posts[1], users[3], 'Could you provide more examples of model relationships?'),
        (posts[2], users[2], 'Templates make frontend development so much easier with Django. Great examples!'),
        (posts[2], users[1], 'I found the class-based views section particularly useful. Thanks!'),
        (posts[3], users[0], 'DRF is amazing for building APIs quickly. Have you tried using ViewSets?'),
        (posts[3], users[3], 'The serializers example was very clear. Looking forward to trying this out.'),
        (posts[4], users[2], 'Django auth system is one of its strongest features. Great breakdown!'),
        (posts[4], users[0], 'The permission system is very flexible. You can create custom permissions too!'),
    ]
    
    for post, author, content in comment_data:
        Comment.objects.create(post=post, author=author, content=content)
    
    print("Mock data created successfully!")
    print(f"Created {len(users)} users")
    print(f"Created {len(posts)} posts") 
    print(f"Created {len(comment_data)} comments")

if __name__ == '__main__':
    create_mock_data()