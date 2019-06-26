from django.urls import path
from . import views
from bookindex import views as bookindexviews

urlpatterns = [
    path('', bookindexviews.indexview, name='index'),
    path('category/<int:category_pk>', views.categoryview, name='category-list'),
]