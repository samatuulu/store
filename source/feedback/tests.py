from django.test import TestCase
from .models import Feedback
from django.contrib.auth import get_user_model
from inventory.models import Product, Category

User = get_user_model()


class FeedbackModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='adam', password='adam123')
        self.category = Category.objects.create(name='Kitchen')

        self.product = Product.objects.create(
            category=self.category,
            name='Mug',
            price=20.00,
            description='Mug for you.'
        )

    def test_feedback_creation(self):
        feedback = Feedback.objects.create(
            user=self.user,
            product=self.product,
            rating=4,
            comment='This is test comment.'
        )

        self.assertIsInstance(feedback, Feedback)
        self.assertEqual(feedback.user, self.user)
        self.assertEqual(feedback.product, self.product)
        self.assertEqual(feedback.rating, 4)
        self.assertEqual(feedback.comment, 'This is test comment.')

    def test_feedback_string_representation(self):
        feedback = Feedback.objects.create(
            user=self.user,
            product=self.product,
            rating=4,
            comment='This is test comment.'
        )

        expected_string = f"Feedback for {self.product.name} by {self.user.username}"
        self.assertEqual(str(feedback), expected_string)
