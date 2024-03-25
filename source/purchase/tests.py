from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Cart, CartItem, Product, Order, OrderItem
from inventory.models import Category


User = get_user_model()


class CartModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='adam', password='adam123')

    def test_cart_creation(self):
        cart = Cart.objects.create(user=self.user)

        self.assertIsInstance(cart, Cart)
        self.assertEqual(cart.user, self.user)
        self.assertEqual(cart.total_price, 0)
        self.assertEqual(cart.status, 'active')

    def test_cart_string_representation(self):
        cart = Cart.objects.create(user=self.user)

        expected_string = f"Cart {cart.id} - User: {self.user.username}"
        self.assertEqual(str(cart), expected_string)


class CartItemModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='adam', password='adam123')

        self.category = Category.objects.create(name='Kitchen')

        self.product = Product.objects.create(
            category=self.category,
            name='Mug',
            price=20.00,
            description='Mug for you.'
        )

        self.cart = Cart.objects.create(user=self.user)

    def test_cart_item_creation(self):
        cart_item = CartItem.objects.create(
            cart=self.cart,
            product=self.product,
            quantity=2,
            price=15.99
        )

        self.assertIsInstance(cart_item, CartItem)
        self.assertEqual(cart_item.cart, self.cart)
        self.assertEqual(cart_item.product, self.product)
        self.assertEqual(cart_item.quantity, 2)
        self.assertEqual(cart_item.price, 15.99)

    def test_cart_item_string_representation(self):
        cart_item = CartItem.objects.create(
            cart=self.cart,
            product=self.product,
            quantity=2,
            price=15.99
        )

        expected_string = f"CartItem {cart_item.id} - Product: {self.product.name}, Quantity: 2"
        self.assertEqual(str(cart_item), expected_string)


class OrderModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='adam', password='adam123')

    def test_order_creation(self):
        order = Order.objects.create(
            user=self.user,
            total_price=50.0,
            status='active',
            delivery_address='Bishkek, Kyrgyzstan',
            payment_method='Credit Card'
        )

        self.assertIsInstance(order, Order)
        self.assertEqual(order.user, self.user)
        self.assertEqual(order.total_price, 50.0)
        self.assertEqual(order.status, 'active')
        self.assertEqual(order.delivery_address, 'Bishkek, Kyrgyzstan')
        self.assertEqual(order.payment_method, 'Credit Card')

    def test_order_string_representation(self):
        order = Order.objects.create(
            user=self.user,
            total_price=50.0,
            status='active',
            delivery_address='Bishkek, Kyrgyzstan',
            payment_method='Credit Card'
        )

        expected_string = f"Order {order.id} - User: {self.user.username}, Status: active"
        self.assertEqual(str(order), expected_string)
