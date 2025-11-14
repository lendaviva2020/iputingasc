from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Booking
from .serializers import BookingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.select_related("customer", "service")
    serializer_class = BookingSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("status", "service")

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_staff:
            return qs
        return qs.filter(customer=self.request.user)

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

    @action(detail=True, methods=("post",), url_path="transition")
    def transition(self, request, pk=None):
        booking = self.get_object()
        new_status = request.data.get("status")
        if new_status not in dict(Booking.Status.choices):
            return Response(
                {"detail": "Status inválido."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if not booking.can_transition_to(new_status):
            return Response(
                {"detail": "Transição de status não permitida."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        booking.status = new_status
        booking.save(update_fields=["status", "updated_at"])
        serializer = self.get_serializer(booking)
        return Response(serializer.data)
