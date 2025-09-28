from django.db import models
# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name   # each row will be displayed using the author name

class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='BookAuthor')
    
    def __str__(self):
        return self.title    # each row will have the title when it is diplayed in admin
    