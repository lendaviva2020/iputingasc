from django.db import models


class TimeStampedModel(models.Model):
    """Modelo base com campos de auditoria comuns."""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ("-created_at",)
