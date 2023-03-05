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