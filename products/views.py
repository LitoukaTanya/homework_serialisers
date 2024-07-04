from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Product, ProductCategory
from products.serializers import ProductsSerializer, ProductCategorySerializer


class ProductsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Product.objects.all()
        return Response(ProductsSerializer(queryset, many=True).data)

@api_view(['GET'])
def product_category_list(request):
    category = ProductCategory.objects.all()
    serializer = ProductCategorySerializer(category, many=True)
    return Response(serializer.data)

