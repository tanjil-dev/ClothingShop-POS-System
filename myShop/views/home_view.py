from django.shortcuts import render, redirect
from myShop.models import *
from myShop.forms.main_form import *
from  django.views import View
from myShop.forms import *

class Home(View):
    template_name = 'myShop/home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class ClothList(View):
    template_name = 'myShop/cloth-list.html'

    def get(self, request):
        data = Product.objects.all().order_by('-id').values()
        context = {
            'data': data
        }
        return render(request, context=context, template_name=self.template_name)

class CreateProduct(View):
    template_name = 'myShop/create-product.html'
    my_form = ProductForm()
    def get(self, request):
        context = {
            'form': self.my_form
        }
        return render(request, context=context, template_name=self.template_name)
    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        context = {
            "msg": "Product %s has been created"%form.cleaned_data['name'],
            "form": self.my_form
        }
        return render(request, context=context, template_name=self.template_name)
class ProductUpdate(View):
    template_name = 'myShop/product-update.html'
    my_form = ProductForm()
    def get(self, request, id):
        data = Product.objects.get(id=id)
        form = ProductForm(instance=data)
        context = {
            'form': form
        }
        return render(request, context=context, template_name=self.template_name)
    def post(self, request, id):
        data = Product.objects.get(id=id)
        form = ProductForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
        context = {
            "msg": "Product %s has been Updated"%form.cleaned_data['name'],
            "form": form
        }
        return render(request, context=context, template_name=self.template_name)

class ProductDelete(View):
    template_name = "myShop/delete-product.html"
    def get(self, request, id):
        data = Product.objects.get(id=id)
        context = {
            'msg': "",
            'data': data
        }
        return render(request, context=context, template_name=self.template_name)

    def post(self, request, id):
        data = Product.objects.get(id=id)
        data.delete()
        return redirect('product-list')

class SalesList(View):
    template_name = 'myShop/sales-list.html'

    def get(self, request):
        data = Sell.objects.all()
        context = {
            'data': data
        }
        return render(request, context=context, template_name=self.template_name)

class SellsUpdate(View):
    template_name = 'myShop/sales-update.html'
    my_form = ProductForm()
    def get(self, request, id):
        data = Sell.objects.get(id=id)
        form = SellsForm(instance=data)
        context = {
            'form': form
        }
        return render(request, context=context, template_name=self.template_name)
    def post(self, request, id):
        data = Sell.objects.get(id=id)
        form = SellsForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
        context = {
            "msg": "Sell %s has been Updated"%form.cleaned_data['product'],
            "form": form
        }
        return render(request, context=context, template_name=self.template_name)

class SellsDelete(View):
    template_name = "myShop/delete-product.html"
    def get(self, request, id):
        data = Sell.objects.get(id=id)
        context = {
            'msg': "",
            'data': data
        }
        return render(request, context=context, template_name=self.template_name)

    def post(self, request, id):
        data = Sell.objects.get(id=id)
        data.delete()
        return redirect('sales-list')

class PurchaseList(View):
    template_name = 'myShop/sales-list.html'

    def get(self, request):
        data = Purchase.objects.all()
        context = {
            'data': data
        }
        return render(request, context=context, template_name=self.template_name)

class CreatePurchase(View):
    template_name = 'myShop/create-product.html'
    my_form = ProductForm()
    def get(self, request):
        context = {
            'form': self.my_form
        }
        return render(request, context=context, template_name=self.template_name)
    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        context = {
            "msg": "Product %s has been created"%form.cleaned_data['name'],
            "form": self.my_form
        }
        return render(request, context=context, template_name=self.template_name)

class PurchaseUpdate(View):
    template_name = 'myShop/sales-update.html'
    my_form = ProductForm()
    def get(self, request, id):
        data = Sell.objects.get(id=id)
        form = SellsForm(instance=data)
        context = {
            'form': form
        }
        return render(request, context=context, template_name=self.template_name)
    def post(self, request, id):
        data = Sell.objects.get(id=id)
        form = SellsForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
        context = {
            "msg": "Sell %s has been Updated"%form.cleaned_data['product'],
            "form": form
        }
        return render(request, context=context, template_name=self.template_name)

class PurchaseDelete(View):
    template_name = "myShop/delete-product.html"
    def get(self, request, id):
        data = Sell.objects.get(id=id)
        context = {
            'msg': "",
            'data': data
        }
        return render(request, context=context, template_name=self.template_name)

    def post(self, request, id):
        data = Sell.objects.get(id=id)
        data.delete()
        return redirect('sales-list')