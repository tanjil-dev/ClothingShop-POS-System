from django.shortcuts import render
from myShop.models import *
from  django.views import View

class Home(View):
    template_name = 'myShop/home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class ClothLst(View):
    template_name = 'myShop/cloth-list.html'

    def get(self, request):
        data = Product.objects.all()
        context = {
            'data': data
        }
        return render(request, context=context, template_name=self.template_name)