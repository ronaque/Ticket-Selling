from rest_framework import viewsets

from ticket_selling_app.models.bus_models import BusTicket
from ticket_selling_app.serializers.bus_serializers import BusTicketSerializer


class BusTicketViewSet(viewsets.ModelViewSet):
    queryset = BusTicket.objects.all()
    serializer_class = BusTicketSerializer