from django.urls import path, include
from . import views
from bookindex import views as bookindexviews
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    path('', bookindexviews.indexview, name='index'),
    path('category/<int:category_pk>', views.categoryview, name='category-list'),
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),

]