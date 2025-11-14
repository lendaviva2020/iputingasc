from django.urls import path

from .views import NotificationPreviewAPIView

app_name = "notifications"

urlpatterns = [
    path(
        "whatsapp/preview/",
        NotificationPreviewAPIView.as_view(),
        name="whatsapp-preview",
    ),
]
