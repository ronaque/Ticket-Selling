from rest_framework import viewsets

from ticket_selling_app.models.bus_models import BusStation
from ticket_selling_app.serializers.bus_serializers import BusStationSerializer


class BusStationViewSet(viewsets.ModelViewSet):
    queryset = BusStation.objects.all()
    serializer_class = BusStationSerializer
