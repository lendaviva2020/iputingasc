from rest_framework import serializers

from .models import GalleryImage


class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = (
            "id",
            "title",
            "description",
            "image_url",
            "thumbnail_url",
            "is_published",
            "created_at",
        )
