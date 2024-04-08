from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def handler404(request, exception):
    template = loader.get_template('main.html')
    return HttpResponseNotFound(template.render())