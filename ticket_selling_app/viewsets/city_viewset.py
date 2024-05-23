from django.http import HttpResponseBadRequest
from rest_framework import viewsets

from ticket_selling_app.models.common_models import City
from ticket_selling_app.serializers.common_serializers import CitySerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        if "name" not in data:
            return HttpResponseBadRequest("City name is required")

        data["name"] = data["name"].title()

        if not City.objects.filter(name=data["name"]).exists():
            return super().create(request, *args, **kwargs)

        return HttpResponseBadRequest("City already exists")
