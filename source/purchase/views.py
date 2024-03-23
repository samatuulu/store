from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from inventory.models import Product

from .models import Cart, CartItem
from .serializers import CartItemSerializer


class AddProductToCartAPIView(APIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return Response({
                'error': 'User not authenticated'
            }, status=status.HTTP_401_UNAUTHORIZED)

        product_id = request.data.get('product_id')
        quantity = int(request.data.get('quantity', 1))

        product = Product.objects.get(pk=product_id)
        cart, created = Cart.objects.get_or_create(user=user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

        if not created:
            cart_item.quantity += quantity
            cart_item.save()

        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data)
