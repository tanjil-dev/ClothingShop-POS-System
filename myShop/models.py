import datetime
import barcode

from io import BytesIO
from django.db import models
from django.contrib.auth.models import User
from django.core.files import File
from barcode.writer import ImageWriter
from django.core.exceptions import ValidationError

CASH = 'CASH'
CARD = 'CARD'
MOBILE_BANKING = 'MOBILE_BANKING'
PAYMENT_TYPE = [(CASH, CASH), (CARD, CARD), (MOBILE_BANKING, MOBILE_BANKING)]

class Company(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'company'

class ClothesCategory(models.Model):
    type = models.CharField(max_length=50)
    category: models.CharField(max_length=50)
    unit = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField(default=None, blank=False)

    def __str__(self):
        return self.type

    class Meta:
        db_table = 'category'

class Product(models.Model):
    name = models.CharField(null=True, blank=True, max_length=100)
    image = models.ImageField(null=True, blank=True)
    bar_code = models.ImageField(null=True, blank=True)
    bar_code_no = models.CharField(max_length=13,blank=True, null=True)
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE, default=None)
    category = models.ForeignKey(ClothesCategory, on_delete=models.CASCADE, default=None)
    buying_price = models.FloatField(default=0)
    selling_price = models.FloatField(default=0)
    quantity = models.PositiveIntegerField(default=None, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        num = 0
        if not self.bar_code:
            EAN = barcode.get_barcode_class('ean13')
            x = datetime.datetime.now()
            y = x.year + x.month + x.day + x.hour + x.minute + x.second + x.microsecond
            num = 1000000000000 + y
            ean1 = EAN('%s'% num, writer=ImageWriter())
            buffer = BytesIO()
            ean1.write(buffer)
            self.bar_code.save('barcode_%s.png'% ean1, File(buffer), save=False)
            self.bar_code_no = ean1
            match = Product.objects.filter(bar_code_no__icontains=self.bar_code_no).values()
            if match:
                raise ValidationError("Barcode already exist!")
            return super().save(*args, **kwargs)
        else:
            return super().save(*args, **kwargs)
    class Meta:
        db_table = 'product'

class Supplier(models.Model):
    supplier_name = models.CharField(max_length=50)
    supplier_address = models.CharField(max_length=50, blank=True, null=True)
    supplier_phone = models.CharField(max_length=50, blank=True, null=True)
    supplier_company_name = models.CharField(max_length=50, blank=True, null=True)

class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None)
    quantity = models.PositiveIntegerField(default=None, blank=False)
    buying_price = models.FloatField(default=0)
    selling_price = models.FloatField(default=0)

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    details = models.CharField(max_length=300, blank=True, null=True)
    total_price = models.PositiveIntegerField(default=None, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    attached_image = models.ImageField(null=True, blank=True)

class Sell(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.FloatField(default=0)
    discount_amount = models.PositiveIntegerField(default=None, blank=False)
    payment_type = models.CharField(max_length=20, choices=PAYMENT_TYPE, default=PAYMENT_TYPE[0][0])
    received_amount = models.FloatField(default=0)
    change_amount = models.FloatField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class ProductSellLog(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sell = models.ForeignKey(Sell, on_delete=models.CASCADE)