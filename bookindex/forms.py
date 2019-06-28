from core.models import Book, Favorite

class FavoriteForm(forms.Form):
    favorited = forms.BooleanField(required=False)