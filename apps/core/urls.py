from django.urls import path

from .views import HealthCheckView, ReadinessProbeView

app_name = "core"

urlpatterns = [
    path("health/", HealthCheckView.as_view(), name="health"),
    path("readiness/", ReadinessProbeView.as_view(), name="readiness"),
]
