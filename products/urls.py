from django.urls import path

from products.views import ProductsAPIView, product_category_list

app_name = 'products'

urlpatterns = [
    path('v1/api/', ProductsAPIView.as_view(), name='products_api'),
    path('categories/v1/api/',product_category_list, name='product_category_list'),
]
