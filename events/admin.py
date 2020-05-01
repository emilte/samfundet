from django.contrib import admin
from django.utils import timezone

from events.models import *
from main import base as main_base

# Register your models here.

class EventAdmin(main_base.CustomBaseAdmin):
    list_display = ['title', 'start', 'place']
    ordering = ['start', 'title']
    list_filter = []
    filter_horizontal = ['participants']
    search_fields = ['title', 'place']


class ParticipantAdmin(admin.ModelAdmin):
    list_display = ['user', 'event', 'date_joined']
    ordering = ['event__start']
    list_filter = []
    readonly_fields = ['date_joined']
    filter_horizontal = []
    search_fields = ['user', 'event']


admin.site.register(Event, EventAdmin)
admin.site.register(Participant, ParticipantAdmin)
