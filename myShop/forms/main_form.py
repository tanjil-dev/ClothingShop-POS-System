from django import forms
from myShop.models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'image', 'company_name', 'category')

class SellsForm(forms.ModelForm):
    class Meta:
        model = Sell
        fields = ('__all__')