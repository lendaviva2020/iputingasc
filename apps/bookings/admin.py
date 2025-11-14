from django.contrib import admin

from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "customer",
        "service",
        "scheduled_for",
        "status",
        "source",
    )
    list_filter = ("status", "source", "scheduled_for")
    search_fields = ("customer__username", "contact_email", "contact_phone")
