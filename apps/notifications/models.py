from django.db import models

from apps.core.models import TimeStampedModel


class NotificationLog(TimeStampedModel):
    class Channel(models.TextChoices):
        EMAIL = "email", "Email"
        WHATSAPP = "whatsapp", "WhatsApp"
        PUSH = "push", "Push"

    class Status(models.TextChoices):
        PENDING = "pending", "Pendente"
        SENT = "sent", "Enviado"
        FAILED = "failed", "Falhou"

    channel = models.CharField(max_length=20, choices=Channel.choices)
    recipient = models.CharField(max_length=255)
    payload = models.JSONField(default=dict)
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.PENDING
    )
    provider_message_id = models.CharField(max_length=120, blank=True)
    error_message = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"{self.channel} -> {self.recipient} ({self.status})"
