from django.urls import path
from myShop.views.home_view import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Home.as_view()),
    path('cloth-list', ClothLst.as_view(), name= 'cloth-list'),
]