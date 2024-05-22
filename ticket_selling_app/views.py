import json

from django.http import (
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponseNotFound,
    HttpResponseServerError,
)
from django.template import TemplateDoesNotExist, loader
from django.views.decorators.http import require_http_methods

from ticket_selling_app.models.common_models import City
from ticket_selling_app.src.bfs import find_path_bfs


@require_http_methods(["GET"])
def main(request):
    try:
        template = loader.get_template("main.html")
        return HttpResponse(template.render())
    except TemplateDoesNotExist:
        return HttpResponseNotFound("Page not found")


@require_http_methods(["GET"])
def path_between_cities(request):
    body = request.read()
    json_body = json.loads(body)
    if len(json_body) != 2:
        return HttpResponseBadRequest("Invalid request")
    if "begin_city" not in json_body or "end_city" not in json_body:
        return HttpResponseBadRequest("Invalid request")
    try:
        begin_city = City.objects.get(name=json_body["begin_city"])
        end_city = City.objects.get(name=json_body["end_city"])
        path = find_path_bfs(begin_city, end_city)
        return HttpResponse(json.dumps(path, default=str))
    except City.DoesNotExist:
        return HttpResponseNotFound("City not found")
    except RuntimeError:
        return HttpResponseNotFound("Path not found")
    except Exception as e:
        return HttpResponseServerError(e)
