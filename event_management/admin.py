from django.contrib import admin

from event_management.models import Event, Ticket

# Register your models here.

admin.site.register(Event)
admin.site.register(Ticket)
