from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.http import require_http_methods
from yaml import loader


@require_http_methods(["GET"])
def main(request):
    try:
        template = loader.get_template('main.html')
        return HttpResponse(template.render())
    except loader.TemplateDoesNotExist:
        return HttpResponseNotFound("Page not found")