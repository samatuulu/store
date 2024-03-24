from django.db import models
from django.contrib.auth import get_user_model

from inventory.models import Product

User = get_user_model()


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedback_user')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='feedback_product')
    rating = models.IntegerField()
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Feedback for {self.product.name} by {self.user.username}"
