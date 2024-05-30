from django.urls import path
from .views import get_product, get_all_products, update_product, delete_product,create_product

urlpatterns = [
    path('products/', get_all_products, name='get_all_products'),
    path('products/<int:product_id>/', get_product, name='get_product'),
    path('products/<int:product_id>/update/', update_product, name='update_product'),
    path('products/<int:product_id>/delete/', delete_product, name='delete_product'),
    path('products/create/', create_product, name='product-create'),
]
