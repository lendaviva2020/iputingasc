from django.conf import settings
from django.db import models

from apps.core.models import TimeStampedModel


class Profile(TimeStampedModel):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    phone_number = models.CharField(max_length=20, blank=True)
    whatsapp_opt_in = models.BooleanField(default=False)
    avatar_url = models.URLField(blank=True)
    bio = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"Profile({self.user.username})"
