from rest_framework import viewsets

from ticket_selling_app.models.plane_models import PlaneTicket
from ticket_selling_app.serializers.plane_serializers import PlaneTicketSerializer


class PlaneTicketViewSet(viewsets.ModelViewSet):
    queryset = PlaneTicket.objects.all()
    serializer_class = PlaneTicketSerializer
