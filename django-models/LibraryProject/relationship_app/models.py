<<<<<<< HEAD
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    ROLES = (
        ("Admin", "Admin"),
        ("Librarian", "Librarian"),
        ("Member", "Member")
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
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
=======
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    ROLES = (
        ("Admin", "Admin"),
        ("Librarian", "Librarian"),
        ("Member", "Member")
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
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
>>>>>>> 9102b10 (blog apps)
        return self.name