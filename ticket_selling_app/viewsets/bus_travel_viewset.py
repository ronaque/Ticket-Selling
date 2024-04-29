from rest_framework import viewsets

from ticket_selling_app.models.bus_models import BusTravel
from ticket_selling_app.serializers.bus_serializers import BusTravelSerializer


class BusTravelViewSet(viewsets.ModelViewSet):
    queryset = BusTravel.objects.all()
    serializer_class = BusTravelSerializer
