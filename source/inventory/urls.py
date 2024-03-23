from django.urls import path

from .views import ProductListCreateView, ProductRetrieveUpdateDestroyView,\
    CategoryListCreateView, CategoryRetrieveUpdateDestroyView

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product_list_create_url'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product_detail_url'),
    path('categories/', CategoryListCreateView.as_view(), name='category_list_create_url'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category_detail_url'),
]
