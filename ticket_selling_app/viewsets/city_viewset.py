from rest_framework import viewsets

from ticket_selling_app.models.common_models import City
from ticket_selling_app.serializers.common_serializers import CitySerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
