from django.shortcuts import render, get_object_or_404
from django.views import generic
from bookindex.models import Book, Category
from django.contrib.auth.decorators import login_required

def indexview(request):

    rawbooks = Book.objects.all()
    books = rawbooks.order_by('date_added')
    categories = Category.objects.all()
    return render(request, 'index.html', {"books": books, "categories": categories})

# class CategoryListView(generic.ListView):
#     model = Category

def categoryview(request, category_pk):

    rawbooks = Book.objects.all()
    books = rawbooks.order_by('date_added')
    categories = Category.objects.all()
    category = get_object_or_404(Category, pk=category_pk)
    return render(request, 'bookindex/category_list.html', {"books": books, "categories": categories, "category": category})
