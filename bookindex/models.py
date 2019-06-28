from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date, time

class Category(models.Model):
    title = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')
    description = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category-list', args=[str(self.id)])

class Book(models.Model):

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, help_text='Enter the summary')
    date_added = models.DateField(null=True, blank=True, default=date.today)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    url = models.URLField(max_length=200, default='https://www.google.com/')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

class Favorite(models.Model):

    book = models.ForeignKey(to=Book, on_delete=models.CASCADE, related_name='favorites')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date_favorited = models.DateField(null=True, blank=True, default=date.today)

