from rest_framework import serializers
from inventory.serializers import ProductSerializer
from .models import CartItem, Cart


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity']


class UserCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id', 'user', 'created_at')
