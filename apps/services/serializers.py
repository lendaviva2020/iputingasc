from rest_framework import serializers

from .models import Service, ServiceCategory


class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = ("id", "name", "description")


class ServiceSerializer(serializers.ModelSerializer):
    category_detail = ServiceCategorySerializer(source="category", read_only=True)

    class Meta:
        model = Service
        fields = (
            "id",
            "title",
            "slug",
            "description",
            "duration_minutes",
            "price",
            "is_active",
            "category",
            "category_detail",
        )
