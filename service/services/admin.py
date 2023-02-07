from django.contrib import admin

from services.models import Service, Subscription


admin.site.register(Service)
admin.site.register(Subscription)

