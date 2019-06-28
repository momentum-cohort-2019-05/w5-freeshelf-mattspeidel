from django.contrib import admin
from bookindex.models import Category, Book, Favorite

# Register your models here.
# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'description', 'date_added', 'category')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(Favorite)   
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'book') 