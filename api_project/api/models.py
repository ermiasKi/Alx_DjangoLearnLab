from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=40)


    def __str__(self):
        return f"{self.title} by {self.author}"