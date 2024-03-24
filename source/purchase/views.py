from django.db.models import Sum

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from inventory.models import Product

from .models import Cart, CartItem, Order, OrderItem
from .serializers import CartItemSerializer, UserCartSerializer, OrderSerializer


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
        price = product.price * quantity
        cart, created = Cart.objects.get_or_create(user=user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product,
                                                            quantity=quantity, price=price)
        if not created:
            cart_item.save()
        total_price = CartItem.objects.aggregate(total_price=Sum('price'))
        total_price_sum = total_price['total_price']
        if total_price_sum is None:
            total_price_sum = 0
        cart.total_price = total_price_sum
        cart.save()

        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data)


class UserCartListAPIView(generics.ListAPIView):
    serializer_class = UserCartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Cart.objects.filter(user=user)


class CreateOrderAPIView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):

        user = request.user
        try:
            cart = Cart.objects.get(user=user)
        except Cart.DoesNotExist:
            return Response({
                'error': 'A user cart does not exist.'
            }, status=status.HTTP_400_BAD_REQUEST)

        price_total = 0
        order = Order.objects.create(user=user, total_price=price_total,
                                     delivery_address=request.data.get("delivery_address"),
                                     payment_method=request.data.get("payment_method"))

        for cart_item in cart.cartitem_set.all():
            order_item = OrderItem.objects.create(order=order, product=cart_item.product,
                                                  quantity=cart_item.quantity, price=cart_item.product.price)
            price_total += cart_item.product.price * cart_item.quantity

        order.total_price = price_total
        order.save()

        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)


class OrderListAPIView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user)
