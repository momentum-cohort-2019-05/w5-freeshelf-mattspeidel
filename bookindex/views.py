from django.shortcuts import render
from django.views import generic
from bookindex.models import Book, Category

# Create your views here.
class IndexListView(generic.ListView):
    def index(self, request):
        model = Book
        return render(request, 'index.html',)

    def get_queryset(self):
        return Book.objects.order_by('date_added')