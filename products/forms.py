from django import forms
from .models import Product

class ProudctForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "title",
            "content",
            "price"
        ]
