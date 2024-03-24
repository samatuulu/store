from django.urls import path

from .views import FeedbackCreateAPIView, FeedbackRetrieveUpdateDestroyAPIView, FeedbackListAPIView


urlpatterns = [
    path('feedback_create/', FeedbackCreateAPIView.as_view(), name='feedback_create'),
    path('feedback_list/', FeedbackListAPIView.as_view(), name='feedback_list'),
    path('feedback_detail/<int:pk>/', FeedbackRetrieveUpdateDestroyAPIView.as_view(), name='feedback_urls')
]
