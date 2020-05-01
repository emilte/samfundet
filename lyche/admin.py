from django.contrib import admin
from django.utils import timezone

from lyche.models import *
from main import base as main_base

class ExampleAdmin(main_base.CustomBaseAdmin):
    list_display = [] # Fields displayed in django admin panel
    ordering = []
    list_filter = [] # Filter on certain fields (right side of list-display)
    filter_horizontal = [] # ManyToManyFields/ForeignKeys
    search_fields = [] # Fields that are searchable


admin.site.register(ExampleModel, ExampleAdmin)
