from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import TimeStampedModel


class Booking(TimeStampedModel):
    class Status(models.TextChoices):
        PENDING = "pending", _("Pendente")
        CONFIRMED = "confirmed", _("Confirmada")
        COMPLETED = "completed", _("Concluída")
        CANCELLED = "cancelled", _("Cancelada")

    class Source(models.TextChoices):
        WEB = "web", _("Site")
        WHATSAPP = "whatsapp", _("WhatsApp")
        WALKIN = "walk_in", _("Presencial")

    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="bookings",
    )
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)
    service = models.ForeignKey(
        "services.Service",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="bookings",
    )
    scheduled_for = models.DateTimeField()
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )
    source = models.CharField(
        max_length=20,
        choices=Source.choices,
        default=Source.WEB,
    )
    total_amount = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    notes = models.TextField(blank=True)
    admin_notes = models.TextField(blank=True)

    class Meta:
        ordering = ("-scheduled_for",)

    def __str__(self) -> str:
        return f"Booking #{self.id} - {self.customer}"

    def can_transition_to(self, new_status: str) -> bool:
        allowed = {
            self.Status.PENDING: {self.Status.CONFIRMED, self.Status.CANCELLED},
            self.Status.CONFIRMED: {self.Status.COMPLETED, self.Status.CANCELLED},
            self.Status.COMPLETED: set(),
            self.Status.CANCELLED: set(),
        }
        return new_status in allowed[self.status]
