from django.utils import timezone
from rest_framework import serializers

from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    customer_username = serializers.CharField(
        source="customer.username", read_only=True
    )

    class Meta:
        model = Booking
        fields = (
            "id",
            "customer",
            "customer_username",
            "contact_email",
            "contact_phone",
            "service",
            "scheduled_for",
            "status",
            "source",
            "total_amount",
            "notes",
            "admin_notes",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("customer", "status", "created_at", "updated_at")

    def validate_scheduled_for(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("A data/hora da reserva deve ser futura.")
        return value

    def create(self, validated_data):
        validated_data["customer"] = self.context["request"].user
        return super().create(validated_data)
