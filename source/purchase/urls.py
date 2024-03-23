from django.urls import path

from .views import AddProductToCartAPIView, UserCartListAPIView


urlpatterns = [
    path('add_product_to_cart/', AddProductToCartAPIView.as_view(), name='add_product_to_cart_url'),
    path('user_cart_list/', UserCartListAPIView.as_view(), name='user_cart_list_url'),

]
