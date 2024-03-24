from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


from .models import Feedback
from .serializers import FeedbackSerializer
from purchase.models import Order
from inventory.models import Product


class FeedbackCreateAPIView(generics.CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):

        user = request.user
        product_id = request.data.get('product_id')
        product = Product.objects.filter(id=product_id).first()
        if product is None:
            return Response({"message": "No product in database."}, status=status.HTTP_400_BAD_REQUEST)

        order = Order.objects.filter(orderitem__product_id=product_id, user_id=user.id).exists()
        if order:
            feedback = Feedback.objects.create(user=user, product=product,
                                               rating=request.data.get('rating'),
                                               comment=request.data.get('comment'))
            return Response(FeedbackSerializer(feedback).data, status=status.HTTP_201_CREATED)
        return Response({'error': "No ordered product by you."}, status=status.HTTP_400_BAD_REQUEST)


class FeedbackListAPIView(generics.ListAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Feedback.objects.filter(user_id=user.id)


class FeedbackRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated]
