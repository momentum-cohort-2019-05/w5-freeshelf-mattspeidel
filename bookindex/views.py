from django.shortcuts import render, get_object_or_404
from django.views import generic
from bookindex.models import Book, Category, Favorite
from django.contrib.auth.decorators import login_required

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

    for favorite in favorites:
        display_books.append(Favorite.book)

    return render(request, 'bookindex/favorites.html', {"user_name": user_name, "display_books": display_books})



