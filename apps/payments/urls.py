from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import PaymentViewSet, StripeWebhookView

router = DefaultRouter()
router.register("", PaymentViewSet, basename="payment")

urlpatterns = [
    path("stripe/webhook/", StripeWebhookView.as_view(), name="stripe-webhook"),
]

urlpatterns += router.urls
