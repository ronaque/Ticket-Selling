import contextlib

from django.apps import apps
from django.contrib import admin

from ticket_selling_app.models.bus_models import *
from ticket_selling_app.models.common_models import *
from ticket_selling_app.models.plane_models import *

models = apps.get_app_config("ticket_selling_app").get_models()
# Register your models here.
for model in models:
    with contextlib.suppress(admin.sites.AlreadyRegistered):
        admin.site.register(model)
