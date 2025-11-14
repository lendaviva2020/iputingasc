from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .services import send_whatsapp_message


class NotificationPreviewAPIView(APIView):
    permission_classes = (permissions.IsAdminUser,)

    def post(self, request, *args, **kwargs):
        phone = request.data.get("phone")
        message = request.data.get("message")
        if not phone or not message:
            return Response(
                {"detail": "Telefone e mensagem são obrigatórios."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        log = send_whatsapp_message(phone, message)
        return Response({"status": log.status, "log_id": log.id})
