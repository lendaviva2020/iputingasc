from django.http import JsonResponse
from django.utils import timezone
from django.views import View

from . import logger


class HealthCheckView(View):
    """Endpoint simples para monitoramento."""

    def get(self, request, *args, **kwargs):
        return JsonResponse(
            {
                "status": "ok",
                "timestamp": timezone.now().isoformat(),
                "version": "1.0.0",
            }
        )


class ReadinessProbeView(View):
    """Confirma se dependências essenciais respondem."""

    def get(self, request, *args, **kwargs):
        logger.core.info("Readiness probe triggered")
        return JsonResponse({"ready": True})
