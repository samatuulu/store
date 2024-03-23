from django.urls import path

from .views import AddProductToCartAPIView


urlpatterns = [
    path('add_product_to_cart/', AddProductToCartAPIView.as_view(), name='add_product_to_cart_url'),
]
