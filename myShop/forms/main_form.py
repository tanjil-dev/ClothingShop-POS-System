from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Column, Row, Fieldset, Div, HTML, ButtonHolder, Submit
from django import forms
from myShop.models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'image', 'company_name', 'category', 'bar_code_no', 'buying_price', 'selling_price', 'quantity')
        widgets = {'bar_code_no': forms.HiddenInput()}

class ProductPosForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductPosForm, self).__init__(*args, **kwargs)
        self.fields['name'].disabled = True

    class Meta:
        model = Product
        fields = ('name', 'quantity', 'selling_price')

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

class Pos(forms.Form):
    number = forms.IntegerField(label= "মোট পণ্য নম্বর লিখুন" , widget=forms.NumberInput(attrs={ 'class' : 'form-control' }))