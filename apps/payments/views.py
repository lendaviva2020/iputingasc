import stripe
from django.conf import settings
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Payment
from .serializers import PaymentSerializer

stripe.api_key = getattr(settings, "STRIPE_SECRET_KEY", "")


class PaymentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Payment.objects.select_related("booking")
    serializer_class = PaymentSerializer
    permission_classes = (permissions.IsAdminUser,)


class StripeWebhookView(APIView):
    authentication_classes = ()
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        payload = request.body
        sig_header = request.META.get("HTTP_STRIPE_SIGNATURE")
        webhook_secret = getattr(settings, "STRIPE_WEBHOOK_SECRET", "")
        try:
            event = stripe.Webhook.construct_event(
                payload=payload,
                sig_header=sig_header,
                secret=webhook_secret,
            )
        except (ValueError, stripe.error.SignatureVerificationError):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        handle_stripe_event(event)
        return Response({"status": "processed"})


def handle_stripe_event(event):
    data = event.get("data", {}).get("object", {})
    Payment.objects.update_or_create(
        provider_payment_id=data.get("id"),
        defaults={
            "amount": data.get("amount", 0) / 100,
            "currency": data.get("currency", "brl").upper(),
            "status": data.get("status", "pending"),
            "raw_payload": data,
        },
    )
