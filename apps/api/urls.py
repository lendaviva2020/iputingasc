from django.urls import include, path

from .views import ApiIndexView

app_name = "api"

urlpatterns = [
    path("", ApiIndexView.as_view(), name="index"),
    path("auth/", include("apps.accounts.urls")),
    path("bookings/", include("apps.bookings.urls")),
    path("services/", include("apps.services.urls")),
    path("gallery/", include("apps.gallery.urls")),
    path("payments/", include("apps.payments.urls")),
    path("notifications/", include("apps.notifications.urls")),
]
