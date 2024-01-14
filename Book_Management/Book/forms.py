from django import forms
from Book.models import BookStoreModel

class BookStoreForm(forms.ModelForm):
    
    class Meta:
        model = BookStoreModel
        exclude = ['First_publication','Last_publication']