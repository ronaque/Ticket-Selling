from django.http import HttpResponse, HttpResponseNotFound
from django.template import TemplateDoesNotExist, loader
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def main(request):
    try:
        template = loader.get_template("main.html")
        return HttpResponse(template.render())
    except TemplateDoesNotExist:
        return HttpResponseNotFound("Page not found")
