from django.test import TestCase
from .models import Product, Category
from decimal import Decimal


class ProductTestCase(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Kitchen')

        self.product = Product.objects.create(
            category=self.category,
            name='Fork',
            price=50.00,
            description='A beautiful, comfortable fork for you.'
        )

    def test_product_creation(self):
        product = Product.objects.get(name='Fork')

        self.assertEqual(product.category, self.category)
        self.assertEqual(product.name, 'Fork')
        self.assertEqual(product.price, 50.00)
        self.assertEqual(product.description, 'A beautiful, comfortable fork for you.')

    def test_product_str_method(self):
        self.assertEqual(str(self.product), 'Fork')

    def test_product_parameter_type(self):
        product = Product.objects.get(name='Fork')

        self.assertIsInstance(product.category.id, int)
        self.assertIsInstance(product.name, str)
        self.assertIsInstance(product.price, Decimal)
        self.assertIsInstance(product.description, str)

    def test_category_creation(self):
        category = Category.objects.get(name='Kitchen')

        self.assertEqual(category, self.category)

    def test_category_str_method(self):
        self.assertEqual(str(self.category), 'Kitchen')

    def test_category_parameter_type(self):
        category = Category.objects.get(name='Kitchen')
        self.assertIsInstance(category.name, str)
