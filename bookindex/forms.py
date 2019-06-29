from django import forms
from bookindex.models import Book, Favorite

class FavoriteForm(forms.Form):
    favorited = forms.BooleanField(required=False)