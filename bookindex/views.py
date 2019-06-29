from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from bookindex.models import Book, Category, Favorite
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from bookindex.forms import FavoriteForm
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.http import HttpResponseRedirect

def indexview(request):

    rawbooks = Book.objects.all()
    books = rawbooks.order_by('date_added')
    categories = Category.objects.all()
    return render(request, 'index.html', {"books": books, "categories": categories})

def categoryview(request, category_pk):

    rawbooks = Book.objects.all()
    books = rawbooks.order_by('date_added')
    categories = Category.objects.all()
    category = get_object_or_404(Category, pk=category_pk)
    return render(request, 'bookindex/category_list.html', {"books": books, "categories": categories, "category": category})

def favoriteview(request, favorite_pk):

    favorite = get_object_or_404(Favorite, pk=favorite_pk)
    user_name = User.objects.get(id=favorite_pk).username
    rawfavorites = request.user.favorite_set.all()
    favorites = rawfavorites.order_by('date_favorited')
    display_books = []

    book = get_object_or_404(Book, pk=favorite_pk)
    user = request.user
   
    favorite, created = user.favorite_set.get_or_create(book=book)

    if created: 
        messages.success(request, f"You've added {book.title} to your favorites.")

    else: 
        messages.info(request, f"You've removed {book.title} from your favorites.")
        favorite.delete()

    for favorite in favorites:
        display_books.append(favorite.book)

    return render(request, 'bookindex/favorites.html', {"user_name": user_name, "display_books": display_books})