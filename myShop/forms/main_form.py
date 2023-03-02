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
class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ('__all__')

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('__all__')

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ('__all__')