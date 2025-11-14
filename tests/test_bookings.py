import datetime

import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone

from apps.bookings.models import Booking
from apps.services.models import Service, ServiceCategory


@pytest.mark.django_db
def test_booking_creation_flow(api_client):
    User = get_user_model()
    user = User.objects.create_user(username="test", password="secret123")
    category = ServiceCategory.objects.create(name="Cortes")
    service = Service.objects.create(
        title="Corte clássico",
        description="Teste",
        price=50,
        category=category,
    )

    api_client.force_authenticate(user=user)
    url = reverse("booking-list")
    payload = {
        "service": service.id,
        "scheduled_for": (timezone.now() + datetime.timedelta(days=1)).isoformat(),
        "contact_email": "t@example.com",
        "contact_phone": "81999999999",
        "notes": "Teste",
    }
    response = api_client.post(url, payload, format="json")
    assert response.status_code == 201
    booking = Booking.objects.get()
    assert booking.customer == user
