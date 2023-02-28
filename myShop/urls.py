from django.urls import path
from myShop.views.home_view import *
from myShop.views.home_view import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #product
    path('', Home.as_view(), name='home'),
    path('cloth-list', ClothList.as_view(), name= 'cloth-list'),
    path('create-product', CreateProduct.as_view(), name= 'create-product'),
    path('product-update/<str:id>/', ProductUpdate.as_view(), name= 'product-update'),
    path('product-delete/<str:id>/', ProductDelete.as_view(), name= 'product-delete'),

    #sales
    path('sales-list', SalesList.as_view(), name= 'sales-list'),
    path('sells-update/<str:id>/', SellsUpdate.as_view(), name= 'sells-update'),
    path('sells-delete/<str:id>/', SellsDelete.as_view(), name= 'sells-delete'),

    #purchase
    path('create-purchase', CreateProduct.as_view(), name= 'create-purchase'),
    path('purchase-list', SalesList.as_view(), name= 'purchase-list'),
    path('purchase/<str:id>/', SellsUpdate.as_view(), name= 'purchase-update'),
    path('purchase/<str:id>/', SellsDelete.as_view(), name= 'purchase-delete'),
]