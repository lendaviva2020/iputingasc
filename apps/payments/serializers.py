from rest_framework import serializers

from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = (
            "id",
            "booking",
            "amount",
            "currency",
            "status",
            "provider",
            "provider_payment_id",
            "created_at",
        )
