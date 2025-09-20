from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _
from ..LibraryProject import settings
from django.contrib.auth.decorators import permission_required

# Create your models here.


class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email must be set'))
        if not username:
            raise ValueError(_('The Username must be set'))
        
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        
        return self.create_user(email, username, password, **extra_fields)
    
@permission_required('relationship_app.can_edit', raise_exception=True)
class CustomUser(AbstractUser):
    objects = CustomUserManager()
    date_of_birth = models.DateField()
    profile_photo = models.ImageField()

    class Meta:
        permissions = [
            ('can_view', 'can view'),
            ('can_create', 'can create'),
            ('can_edit', 'can edit'),
            ('can_delete', 'can delete'),
        ]


class UserProfile(models.Model):
    ROLES = (
        ("Admin", "Admin"),
        ("Librarian", "Librarian"),
        ("Member", "Member")
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    role = models.CharField(max_length=20, choices=ROLES, default='Member')


    def __str__(self):
        return f"{self.user.username} - {self.role}"
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

class Author(models.Model):
    name = models.CharField(max_length=250)


    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=210)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.title} by {self.author}"
    
    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]

class Library(models.Model):
    name = models.CharField(max_length=250)
    books = models.ManyToManyField('Book')

class Librarian(models.Model):
    name = models.CharField(max_length=210)
    library = models.OneToOneField('Library', on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.name