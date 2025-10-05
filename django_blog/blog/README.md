# Django Blog Application

A feature-rich blog platform built with Django, featuring user authentication, post/comments CRUD, tagging, and search functionality.

## ✨ Features

- **Authentication**: User registration, login/logout, editable profiles, secure password handling, CSRF protection.
- **Blog Posts**: CRUD operations, rich text support, draft/publish status, automatic author assignment, tags.
- **Comments**: Nested comments, CRUD with author permissions, edit history, moderation.
- **Tagging**: Flexible tags, filtering, tag pages, automatic creation.
- **Search**: Full-text search across titles, content, tags; paginated results.
- **Security**: Authentication-based access, author permissions, CSRF protection, secure password storage.

## 📁 Project Structure

```
django_blog/
├── blog/
│   ├── migrations/
│   ├── templates/blog/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── profile.html
│   │   ├── post_list.html
│   │   ├── post_detail.html
│   │   ├── post_form.html
│   │   ├── comment_form.html
│   │   ├── search_results.html
│   │   └── posts_by_tag.html
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── django_blog/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── requirements.txt
```

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- Django 5.2+
- Virtual environment

### Setup
1. Clone the repo:
   ```bash
   git clone <repository-url>
   cd django_blog
   ```
2. Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install django
   ```
4. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Create superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```
6. Start server:
   ```bash
   python manage.py runserver
   ```
7. Access:
   - Site: http://127.0.0.1:8000/
   - Admin: http://127.0.0.1:8000/admin/

## 🎯 Usage

- **Visitors**: Browse posts, read details, search, filter by tags.
- **Users**: Register/login, create/edit posts, add/edit comments, manage profile.
- **Admins**: Manage all content via `/admin/`.

## 🔧 API Testing
- Get CSRF token: `GET /get-csrf-token/`
- Include `X-CSRFToken: <token>` in POST headers.
- Maintain session with cookies.

## 🎨 Styling
- Responsive custom CSS
- Consistent color scheme
- Mobile-friendly
- Interactive elements

## 🔒 Security
- CSRF protection
- Authentication requirements
- Author-based permissions
- Secure password storage
- SQL injection protection via Django ORM

## 📊 Database Schema
```
User
├── username
├── email
├── password
└── profile fields

Post
├── title
├── content
├── author (FK → User)
├── published_date
├── published
└── tags (M2M → Tag)

Comment
├── post (FK → Post)
├── author (FK → User)
├── content
├── created_at
└── updated_at

Tag
├── name (unique)
└── created_at
```

## 🧪 Testing
- **Manual**: Test registration, CRUD, permissions, search, responsiveness.
- **Automated**: Run `python manage.py test`.

## 🚀 Deployment
- Set `DEBUG = False`
- Use PostgreSQL
- Configure static files, allowed hosts, SSL
- Use Gunicorn + Nginx
- Set environment variables: `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, `DATABASE_URL`, `EMAIL_BACKEND`

## 🤝 Contributing
1. Fork repo
2. Create feature branch
3. Make changes and add tests
4. Submit pull request

## 📝 License
MIT License

## 🆘 Support
- Check Django docs
- Review code comments
- Open an issue

**Built with ❤️ using Django**s