from django.db import models

from apps.core.models import TimeStampedModel


class GalleryImage(TimeStampedModel):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image_url = models.URLField()
    thumbnail_url = models.URLField(blank=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return self.title
