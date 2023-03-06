from django.shortcuts import render, redirect
from myShop.models import *
from myShop.forms.main_form import *
from  django.views import View
from myShop.forms import *
from myShop.filters import *
from myShop.services.barcode_service import *


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
            'data': data
        }
        return render(request, context=context, template_name=self.template_name)

    def post(self, request, id):
        data = Sell.objects.get(id=id)
        data.delete()
        return redirect('sales-list')

class PurchaseList(View):
    template_name = 'myShop/purchase-list.html'

    def get(self, request):
        data = Purchase.objects.all()
        context = {
            'data': data
        }
        return render(request, context=context, template_name=self.template_name)

class CreatePurchase(View):
    template_name = 'myShop/create-purchase.html'
    my_form = PurchaseForm()
    def get(self, request):
        context = {
            'form': self.my_form
        }
        return render(request, context=context, template_name=self.template_name)
    def post(self, request):
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
        context = {
            "msg": "Product %s has been created"%form.cleaned_data['product'],
            "form": self.my_form
        }
        return render(request, context=context, template_name=self.template_name)

class PurchaseUpdate(View):
    template_name = 'myShop/purchase-update.html'
    my_form = PurchaseForm()
    def get(self, request, id):
        data = Purchase.objects.get(id=id)
        form = PurchaseForm(instance=data)
        context = {
            'form': form
        }
        return render(request, context=context, template_name=self.template_name)
    def post(self, request, id):
        data = Purchase.objects.get(id=id)
        form = PurchaseForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
        context = {
            "msg": "Purchase %s has been Updated"%form.cleaned_data['product'],
            "form": form
        }
        return render(request, context=context, template_name=self.template_name)

class PurchaseDelete(View):
    template_name = "myShop/delete-purchase.html"
    def get(self, request, id):
        data = Purchase.objects.get(id=id)
        context = {
            'data': data
        }
        return render(request, context=context, template_name=self.template_name)

    def post(self, request, id):
        data = Purchase.objects.get(id=id)
        data.delete()
        return redirect('purchase-list')

class ExpenseList(View):
    template_name = 'myShop/expense-list.html'

    def get(self, request):
        data = Expense.objects.all().order_by('-id').values()
        context = {
            'data': data
        }
        return render(request, context=context, template_name=self.template_name)

class CreateExpense(View):
    template_name = 'myShop/create-expense.html'
    my_form = ExpenseForm()
    def get(self, request):
        context = {
            'form': self.my_form
        }
        return render(request, context=context, template_name=self.template_name)
    def post(self, request):
        form = ExpenseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        context = {
            "msg": "Product %s has been created"%form.cleaned_data['details'],
            "form": self.my_form
        }
        return render(request, context=context, template_name=self.template_name)
class ExpenseUpdate(View):
    template_name = 'myShop/product-update.html'
    my_form = ExpenseForm()
    def get(self, request, id):
        data = Expense.objects.get(id=id)
        form = ExpenseForm(instance=data)
        context = {
            'form': form
        }
        return render(request, context=context, template_name=self.template_name)
    def post(self, request, id):
        data = Expense.objects.get(id=id)
        form = ExpenseForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
        context = {
            "msg": "Product %s has been Updated"%form.cleaned_data['details'],
            "form": form
        }
        return render(request, context=context, template_name=self.template_name)

class ExpenseDelete(View):
    template_name = "myShop/delete-product.html"
    def get(self, request, id):
        data = Expense.objects.get(id=id)
        context = {
            'data': data
        }
        return render(request, context=context, template_name=self.template_name)

    def post(self, request, id):
        data = Expense.objects.get(id=id)
        data.delete()
        return redirect('expense-list')

class SupplierList(View):
    template_name = 'myShop/supplier-list.html'

    def get(self, request):
        data = Supplier.objects.all()
        context = {
            'data': data
        }
        return render(request, context=context, template_name=self.template_name)

class CreateSupplier(View):
    template_name = 'myShop/create-supplier.html'
    my_form = SupplierForm()
    def get(self, request):
        context = {
            'form': self.my_form
        }
        return render(request, context=context, template_name=self.template_name)
    def post(self, request):
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
        context = {
            "msg": "Product %s has been created"%form.cleaned_data['supplier_name'],
            "form": self.my_form
        }
        return render(request, context=context, template_name=self.template_name)

class SupplierUpdate(View):
    template_name = 'myShop/supplier-update.html'
    my_form = SupplierForm()
    def get(self, request, id):
        data = Supplier.objects.get(id=id)
        form = SupplierForm(instance=data)
        context = {
            'form': form
        }
        return render(request, context=context, template_name=self.template_name)
    def post(self, request, id):
        data = Supplier.objects.get(id=id)
        form = SupplierForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
        context = {
            "msg": "Supplier %s has been Updated"%form.cleaned_data['supplier_name'],
            "form": form
        }
        return render(request, context=context, template_name=self.template_name)

class SupplierDelete(View):
    template_name = "myShop/delete-supplier.html"
    def get(self, request, id):
        data = Supplier.objects.get(id=id)
        context = {
            'data': data
        }
        return render(request, context=context, template_name=self.template_name)

    def post(self, request, id):
        data = Supplier.objects.get(id=id)
        data.delete()
        return redirect('supplier-list')

class pos(View):
    template_name = 'myShop/pos.html'
    my_form = ProductPosForm()
    def get(self, request):

        context = {

        }
        return render(request, context=context, template_name=self.template_name)

    def post(self, request):
        global form2
        data = []
        if int(request.POST['number']) >=1 and request.POST['number']:
            form1 = Pos(request.POST)
            if form1.is_valid():
                for n in range(form1.cleaned_data['number']):
                    barcode_num = getBarCodeNumber()
                    product = Product.objects.filter(bar_code_no=barcode_num).values()
                    form2 = ProductPosForm(instance=data)
                    data.append(product)
        else:
            form2 = ProductPosForm(request.POST)

        context = {
            'form': form2
        }
        return render(request, context=context, template_name=self.template_name)

class PrintBarcode(View):
    template_name = "myShop/print-barcode.html"
    def get(self, request):
        data = Product.objects.all()
        myFilter = ProductFilter(request.GET, queryset=data)
        data = myFilter.qs
        context = {
            'data': data,
            'myFilter': myFilter,
        }
        return render(request, context=context, template_name=self.template_name)