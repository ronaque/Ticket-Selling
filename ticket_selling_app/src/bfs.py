from django.forms import model_to_dict

from ticket_selling_app.models.bus_models import BusTravel
from ticket_selling_app.models.common_models import City
from ticket_selling_app.models.plane_models import PlaneTravel


def construct_path(node: tuple, end_node: City, path: list, visited: set):
    if node[1] == end_node:
        return path.append((node[0], end_node))

    visited.add(node)
    path.append(node)

    # Get Travels that depart from current city
    plane_travels = PlaneTravel.objects.filter(
        airport_departure_id__city=node[1]
    ).select_related("airport_arrival_id__city")
    bus_travels = BusTravel.objects.filter(
        bus_station_departure_id__city=node[1]
    ).select_related("bus_station_arrival_id__city")

    travel_city_tuples = []

    # Add neighbours cities travel
    for plane_travel in plane_travels:
        travel_tuple = (plane_travel, plane_travel.airport_arrival_id.city)
        if travel_tuple not in visited:
            travel_city_tuples.append(travel_tuple)

    for bus_travel in bus_travels:
        travel_tuple = (bus_travel, bus_travel.bus_station_arrival_id.city)
        if travel_tuple not in visited:
            travel_city_tuples.append(travel_tuple)

    for neighbor in travel_city_tuples:
        construct_path(neighbor, end_node, path, visited)
        if path[-1][1] == end_node:
            return path

    visited.remove(node)
    path.pop()
    return path


def find_path_bfs(begin_node: City, end_node: City):
    path = []
    visited = set()

    path = construct_path((None, begin_node), end_node, path, visited)

    if not path:
        raise RuntimeError("Path not found")

    result = {}
    for idx, path_travel in enumerate(path):
        if path_travel[0] is None:
            result[idx] = ["begin", model_to_dict(path_travel[1])]
        else:
            result[idx] = [model_to_dict(path_travel[0]), model_to_dict(path_travel[1])]

    return result
