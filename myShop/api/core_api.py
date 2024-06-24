import json
import re

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from myShop.models import *
from myShop.serializer.core_serializer import *

class ProductAPI(APIView):
    def get(self, request, *args, **kwargs):
        term = request.GET.get('term', None)
        data = Product.objects.get(bar_code_no=term)
        if data:
            serializer = ProductSerializer(data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response("Data Not found", status=status.HTTP_404_NOT_FOUND)

class SellProductAPI(APIView):
    def post(self, request, *args, **kwargs):
        total = request.POST['total']
        discount = request.POST['discount']
        if not discount:
            discount = 0
        after_discount = request.POST['after_discount']
        received_amount = request.POST['received_amount']
        change_amount = request.POST['change_amount']
        payment_type = request.POST['payment_type']
        product_id = request.POST['product_id']
        print(product_id)
        json.loads(product_id)
        print(type(product_id))
        num = re.findall(r'\d+', product_id)
        if len(received_amount) == 0:
            return Response("Sell Incomplete", status=status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
            data = Sell.objects.create(total_price=total, discount_amount=discount, payment_type=payment_type,
                                       received_amount=received_amount, change_amount=change_amount,
                                       after_discount=after_discount)
            for i in num:
                ProductSellLog.objects.create(sell_id=data.id, product_id=i)
            return Response("Sell Success", status=status.HTTP_201_CREATED)