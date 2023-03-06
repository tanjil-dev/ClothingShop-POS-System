from django.urls import path
from myShop.views.home_view import *
from myShop.views.home_view import *
from myShop.api.core_api import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #product
    # path('', Home.as_view(), name='home'),
    path('cloth-list', ClothList.as_view(), name= 'cloth-list'),
    path('create-product', CreateProduct.as_view(), name= 'create-product'),
    path('product-update/<str:id>/', ProductUpdate.as_view(), name= 'product-update'),
    path('product-delete/<str:id>/', ProductDelete.as_view(), name= 'product-delete'),
    path('print-barcode', PrintBarcode.as_view(), name= 'print-barcode'),

    #sales
    path('', pos.as_view(), name= 'pos'),
    path('sales-list', SalesList.as_view(), name= 'sales-list'),
    path('sells-update/<str:id>/', SellsUpdate.as_view(), name= 'sells-update'),
    path('sells-delete/<str:id>/', SellsDelete.as_view(), name= 'sells-delete'),

    #purchase
    path('create-purchase', CreatePurchase.as_view(), name= 'create-purchase'),
    path('purchase-list', PurchaseList.as_view(), name= 'purchase-list'),
    path('purchase/<str:id>/', PurchaseUpdate.as_view(), name= 'purchase-update'),
    path('purchase/<str:id>/', PurchaseDelete.as_view(), name= 'purchase-delete'),

    #expense
    path('create-expense', CreateExpense.as_view(), name= 'create-expense'),
    path('expense-list', ExpenseList.as_view(), name= 'expense-list'),
    path('expense/<str:id>/', ExpenseUpdate.as_view(), name= 'expense-update'),
    path('expense/<str:id>/', ExpenseDelete.as_view(), name= 'expense-delete'),

    #supplier
    path('create-supplier', CreateSupplier.as_view(), name= 'create-supplier'),
    path('supplier-list', SupplierList.as_view(), name= 'supplier-list'),
    path('supplier/<str:id>/', SupplierUpdate.as_view(), name= 'supplier-update'),
    path('supplier/<str:id>/', SupplierDelete.as_view(), name= 'supplier-delete'),

    #apis
    path('get-product/', ProductAPI.as_view(), name='get-product'),
]