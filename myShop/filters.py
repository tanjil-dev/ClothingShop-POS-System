import django_filters
from django.forms import DateInput
from django import forms


from myShop.models import *

class ProductFilter(django_filters.FilterSet):
    created_at = django_filters.DateFilter(
        lookup_expr='icontains',
        widget=forms.DateInput(
            attrs={
                'id': 'datepicker',
                'type': 'text'
            }
        )
    )
    class Meta:
        model = Product
        fields = ('name', 'bar_code_no', 'selling_price', 'created_at')