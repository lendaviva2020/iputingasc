from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView


class ApiIndexView(APIView):
    authentication_classes = ()
    permission_classes = (permissions.AllowAny,)

    def get(self, request, *args, **kwargs):
        return Response(
            {
                "message": "API do Iputinga Social e Cultural",
                "resources": [
                    "/api/auth/",
                    "/api/bookings/",
                    "/api/services/",
                    "/api/gallery/",
                    "/api/payments/",
                    "/api/notifications/",
                ],
            }
        )
