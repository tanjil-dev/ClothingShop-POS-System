from django.contrib import admin
from .models import *

admin.site.register(Product)
admin.site.register(ClothesCategory)
admin.site.register(Company)
admin.site.register(Supplier)
admin.site.register(Expense)
admin.site.register(Sell)
admin.site.register(Purchase)