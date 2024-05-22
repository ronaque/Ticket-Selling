"""TicketSelling URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from ticket_selling_app import views
from ticket_selling_app.viewsets.airport_viewset import AirportViewSet
from ticket_selling_app.viewsets.bus_station_viewset import BusStationViewSet
from ticket_selling_app.viewsets.bus_ticket_viewset import BusTicketViewSet
from ticket_selling_app.viewsets.bus_travel_viewset import BusTravelViewSet
from ticket_selling_app.viewsets.bus_viewset import BusViewSet
from ticket_selling_app.viewsets.city_viewset import CityViewSet
from ticket_selling_app.viewsets.plane_ticket_viewset import PlaneTicketViewSet
from ticket_selling_app.viewsets.plane_travel_viewsets import PlaneTravelViewSet
from ticket_selling_app.viewsets.plane_viewset import PlaneViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Ticket Selling",
        default_version="V1",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()
router.register(r"city", CityViewSet, basename="city")
router.register(r"bus-station", BusStationViewSet, basename="bus-station")
router.register(r"bus", BusViewSet, basename="bus")
router.register(r"bus-ticket", BusTicketViewSet, basename="bus-ticket")
router.register(r"bus-travel", BusTravelViewSet, basename="bus-travel")
router.register(r"airport", AirportViewSet, basename="airport")
router.register(r"plane", PlaneViewSet, basename="plane")
router.register(r"plane-ticket", PlaneTicketViewSet, basename="plane-ticket")
router.register(r"plane-travel", PlaneTravelViewSet, basename="plane-travel")
urlpatterns = [
    path("", views.main, name="index"),
    path("api/", include(router.urls)),
    path("admin/", admin.site.urls),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("search-path/", views.path_between_cities, name="search-path"),
]
