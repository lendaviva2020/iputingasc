from django.contrib import admin

from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("id", "provider", "status", "amount", "currency", "created_at")
    list_filter = ("status", "provider")
    search_fields = ("provider_payment_id",)
