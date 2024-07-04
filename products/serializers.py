from rest_framework import serializers

from products.models import Product, ProductCategory


class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'description')


class ProductCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = ('id', 'name', 'description')