from rest_framework import viewsets, permissions

from ticket_selling_app.models.plane_models import Airport
from ticket_selling_app.serializers.plane_serializers import AirportSerializer


class AirportViewSet(viewsets.ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer